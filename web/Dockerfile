FROM golang:1.19.1-alpine3.16
RUN apk add --no-cache git gcc musl-dev
WORKDIR /build
COPY go.mod .
#COPY go.sum .
RUN go mod download
COPY . .
RUN go build -o /words /build/cmd

FROM alpine:3.16
RUN apk add --no-cache ca-certificates
COPY --from=0 /words /words
CMD ["/words"]
