# Design

---

## Arch

- _Options_:
  - Monolithic Not complicated
  - Micro chucking into smaller reusable parts
- _Decision_: **_Monolithic_**

## Hosted

- _Options_:
  - Heroku: that's where my website is already hosted and I don't have to create a new domain just a new page
  - AWS: familiar with this framework
  - AZURE: familiar with this framework
  - Google Cloud: it would be fun to try
- _Decision_: **_Heroku_**

## Language(s)

- _Options_:
  - Python: I'm very familiar wih the language for sc ripting however not a web application
  - Java: I'm very familiar with the language however not gr eat for frontend work, I already created a cli version
  - ReactJS: I'm familiar with Javascript and the UX li brary frontend will be easiest with and my resume is in react
- _Decision_: **_Java backend with React Frontend_**

## Build Tool

- _Options_:
- Gradle is easier to read
- Maven is the standard at work
- _Decision_: **_Java backend with React Frontend_**

## Database

- _Options_:
  - Postgres: its already on my compute
  - MySQL ususally use it at work
- _Decision_: **_Postgres_**

## authentication

- _Options_:
  - JWT authentication
  - OpenID Connect server with Keycloak
  - HTTP Session Authentication
- _Decision_: **_JWT_**

## cache abstraction

- _Options_:
  - Hibernate 2nd level cache
  - caffine
  - hazelnut
  - reddis
- _Decision_: **_Hibernate_**

## libraries/api

- _Options_:
  - [dog-ceo-api](https://github.com/ElliottLandsborough/dog-ceo-api) already created api database easy to add on but incomplete for this project
  - Swagger don't need
  - elastic don't need
  - websockets don't need
  - kafka don't need
- _Decision_: **_fork dog ceo api and possibily add the information needed_**

## Frameworks

- _Options_:
  - Angular familiar
  - React familiar
  - Vue
  - Spring familiar
  - Micronaut
  - Quarkus
- _Decision_: Spring and React

## Bootswatch Theme

- _Options_:
  - Cyborg
  - Lux
  - Slate
  - Solar
  - Superhero
  - United
  - Yeti
- _Decision_: Yeti
