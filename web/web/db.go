package web

import "time"

type DBRecord struct {
	Word    string   `json:"word"`
	Similar []string `json:"similar"`
}

var db []DBRecord

const ourEpoch = 1669150800 // Thu Nov 24 2022 00:00:00 GMT+0300 (GMT+03:00)

func currentGame() int {
	return (int(time.Now().Unix()) - ourEpoch) / 86400
}
