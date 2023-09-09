package main

import (
    "log"
    "net/http"
)

func main() {

    port := ":8080"
    http.HandleFunc("/redis", func(w http.ResponseWriter, r *http.Request) {
        w.Write([]byte("Use redis"))
    })
    log.Fatal(http.ListenAndServe(port, nil))
}
