# "environ" - the environment app

When you implement a bunch of applications for a company then watching them and configuring them becomes cumbersome. E.g.
your mail server might need to change because it suddenly crashes. But you have like 20 apps on different systems. 
Not likely that you want to do the job manually.

That is why you need an environment. Something that gives you access to configuration and logging.

- there is a way to store configuration values
- there is a way for your applications to request cnfiguration values
- there is a way to receive and save log messages from all you applications
