# CHATEYE👁️

**Anonymous telegram bot written on python/aiogram**
- Free template for usage
- Bot using postgresql deployed on heroku servers

# SQL STRUCTURE
- first table structure:
```
  CREATE TABLE IF NOT EXISTS public.dialogs
  (
      id integer NOT NULL DEFAULT nextval('dialogs_id_seq'::regclass),
      firstuser character varying COLLATE pg_catalog."default",
      seconduser character varying COLLATE pg_catalog."default",
      CONSTRAINT dialogs_pkey PRIMARY KEY (id)
  )
```
- second table structure:

```
  CREATE TABLE IF NOT EXISTS public.queue
(
    id integer NOT NULL DEFAULT nextval('queue_id_seq'::regclass),
    firstuser character varying COLLATE pg_catalog."default",
    seconduser character varying COLLATE pg_catalog."default",
    CONSTRAINT queue_pkey PRIMARY KEY (id)
)
```
