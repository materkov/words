package web

import (
	"encoding/json"
	"log"
	"net/http"
	"os"
)

type Response struct {
	Error    string      `json:"error,omitempty"`
	Response interface{} `json:"response,omitempty"`
}

func writeErr(w http.ResponseWriter, err string) {
	_ = json.NewEncoder(w).Encode(Response{Error: err})
}

func writeResp(w http.ResponseWriter, r interface{}) {
	_ = json.NewEncoder(w).Encode(Response{Response: r})
}

type Game struct {
	ID          int `json:"id"`
	MaxDistance int `json:"maxDistance"`
}

type GameGroup struct {
	Language string `json:"language"`
	Games    []Game `json:"games"`
}

type getGameStateResp struct {
	GameGroups []GameGroup `json:"gameGroups"`
}

func getGameState(w http.ResponseWriter, r *http.Request) {
	curGame := currentGame()

	var games []Game
	for i := 1; i <= curGame; i++ {
		games = append(games, Game{
			ID:          i,
			MaxDistance: len(db[i-1].Similar),
		})
	}

	resp := Response{
		Response: getGameStateResp{
			GameGroups: []GameGroup{
				{
					Language: "ru",
					Games:    games,
				},
			},
		},
	}
	_ = json.NewEncoder(w).Encode(resp)
}

type checkWordReq struct {
	GameID    int    `json:"gameId"`
	WordValue string `json:"wordValue"`
}

type checkWordResp struct {
	IsFounded bool `json:"isFounded"`
	Distance  int  `json:"distance"`
}

func checkWord(w http.ResponseWriter, r *http.Request) {
	req := checkWordReq{}
	_ = json.NewDecoder(r.Body).Decode(&req)

	if req.GameID <= 0 || req.GameID > currentGame() {
		writeErr(w, "Incorrect game ID")
		return
	}
	if req.WordValue == "" {
		writeErr(w, "Empty word")
		return
	}

	if req.WordValue == db[req.GameID-1].Word {
		writeResp(w, checkWordResp{
			Distance: 0,
		})
		return
	}

	similar := db[req.GameID-1].Similar

	found := -1
	for i, item := range similar {
		if item == req.WordValue {
			found = i
			break
		}
	}
	if found == -1 {
		writeResp(w, checkWordResp{
			Distance: -1,
		})
		return
	}

	writeResp(w, checkWordResp{
		Distance: found + 1,
	})
	return
}

type getTipReq struct {
	GameID   int `json:"gameId"`
	Distance int `json:"distance"`
}

type getTipResponse struct {
	WordValue string `json:"word"`
}

func getTip(w http.ResponseWriter, r *http.Request) {
	req := getTipReq{}
	_ = json.NewDecoder(r.Body).Decode(&req)

	if req.GameID <= 0 || req.GameID > currentGame() {
		writeErr(w, "Incorrect game ID")
		return
	}

	if req.Distance == 0 {
		writeResp(w, getTipResponse{WordValue: db[req.GameID-1].Word})
		return
	}

	similar := db[req.GameID-1].Similar
	neededIdx := req.Distance - 1

	if neededIdx < 0 || req.Distance >= len(similar) {
		writeErr(w, "Incorrect distance")
		return
	}

	writeResp(w, getTipResponse{WordValue: similar[neededIdx]})
}

type giveUpReq struct {
	GameID int `json:"gameId"`
}

type giveUpResp struct {
	WordValue    string   `json:"wordValue"`
	SimilarWords []string `json:"similarWords"`
}

func giveUp(w http.ResponseWriter, r *http.Request) {
	req := giveUpReq{}
	_ = json.NewDecoder(r.Body).Decode(&req)

	if req.GameID <= 0 || req.GameID > currentGame() {
		writeErr(w, "Incorrect game ID")
		return
	}

	similar := db[req.GameID-1].Similar
	if len(similar) > 500 {
		similar = similar[:500]
	}

	writeResp(w, giveUpResp{
		WordValue:    db[req.GameID-1].Word,
		SimilarWords: similar,
	})
}

func Serve() {
	log.Printf("Reading DB...")

	//dat, err := os.ReadFile("/Users/m.materkov/projects/words/results2.txt")
	dat, err := os.ReadFile("/apps/words/results2.txt")
	if err != nil {
		log.Fatalf("Error opening DB: %s", err)
	}

	err = json.Unmarshal(dat, &db)
	if err != nil {
		log.Fatalf("Error parsing DB: %s", err)
	}

	log.Printf("Done reading DB")

	http.HandleFunc("/getGameState", getGameState)
	http.HandleFunc("/checkWord", checkWord)
	http.HandleFunc("/getTip", getTip)
	http.HandleFunc("/giveUp", giveUp)

	http.ListenAndServe("127.0.0.1:8736", nil)
}
