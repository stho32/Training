# "environ" - the environment app

When you implement a bunch of applications for a company then watching them and configuring them becomes cumbersome. E.g.
your mail server might need to change because it suddenly crashes. But you have like 20 apps on different systems. 
Not likely that you want to do the job manually.

That is why you need an environment. Something that gives you access to configuration and logging.

- [ ] (R001) the app has a web ui
    - [ ] (R002) there is a way to store configuration values
        - [ ] (R003) there is a ui that allows for entering of configuration values
        - [ ] (R004) there is the possibility of persisting configuration values between sessions
            - [ ] (R005) one option is an encrypted file
                - [ ] (R006) when you fire up the application it will ask you for the password for the encrypted file
                - [ ] (R007) when you give it the right password it will enable all other functionality, but not before

    - [ ] (R008) there is a way to look up the received log messages
        - [ ] (R010) log messages are stored in memory
    - [ ] (R011) log messages are removed after some time

- [ ] (R012) the app has a web api
    - [ ] (R013) there is a way to receive and save log messages from all you applications
    - [ ] (R014) there is a way for your applications to request configuration values

- [ ] (R015) the web api uses api keys
- [ ] (R016) there is a log of which api key has requested which configuration value when

- [ ] (R017) the complete web application is only accessable from localhost


