version: '2'
services:
    app:
        build: .
        volumes:
            - .:/web