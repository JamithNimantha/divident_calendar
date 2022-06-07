CREATE TABLE IF NOT EXISTS public.dividend_calendar
(
    symbol character varying(10) COLLATE pg_catalog."default" NOT NULL,
	ex_date character varying(15) COLLATE pg_catalog."default",
	dvidend numeric(10,2),
	payment_date date,
    record_date date,
    announcement_date date,
	annual_dividend numeric(10,2),
    company_name character varying(250) COLLATE pg_catalog."default",
	update_date date,
    update_time time without time zone,
    CONSTRAINT dividend_calendar_pkey PRIMARY KEY (symbol,ex_date)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.dividend_calendar
    OWNER to postgres;