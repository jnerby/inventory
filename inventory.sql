--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: entries; Type: TABLE; Schema: public; Owner: jnerby
--

CREATE TABLE public.entries (
    entry_id integer NOT NULL,
    product_name character varying(50) NOT NULL,
    qty integer NOT NULL,
    "timestamp" timestamp without time zone
);


ALTER TABLE public.entries OWNER TO jnerby;

--
-- Name: entries_entry_id_seq; Type: SEQUENCE; Schema: public; Owner: jnerby
--

CREATE SEQUENCE public.entries_entry_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.entries_entry_id_seq OWNER TO jnerby;

--
-- Name: entries_entry_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jnerby
--

ALTER SEQUENCE public.entries_entry_id_seq OWNED BY public.entries.entry_id;


--
-- Name: entries entry_id; Type: DEFAULT; Schema: public; Owner: jnerby
--

ALTER TABLE ONLY public.entries ALTER COLUMN entry_id SET DEFAULT nextval('public.entries_entry_id_seq'::regclass);


--
-- Data for Name: entries; Type: TABLE DATA; Schema: public; Owner: jnerby
--

COPY public.entries (entry_id, product_name, qty, "timestamp") FROM stdin;
1	Men's Sweaters	500	2021-01-08 12:16:30.311548
2	Men's T-Shirts	500	2021-01-08 12:16:38.152827
3	Women's Maxi Dresses	5000	2021-01-08 12:17:01.426941
4	Women's Bootcut Jeans	600	2021-01-08 12:15:57.925399
5	Mens's Joggers	400	2021-01-08 12:15:57.925399
6	Women's Wool Socks	400	2021-01-08 12:15:57.925399
7	Women's Joggers	1000	2021-01-08 12:15:32.148166
8	Women's Sweatshirts	1000	2021-01-08 12:15:40.037055
9	Women's Bomber Jackets	3000	2021-01-08 12:15:49.610643
10	Women's Chelsea Boots	400	2021-02-08 12:15:57.925399
11	Women's Leggings	5000	2021-02-08 12:16:04.664318
12	Men's Wool Socks	100	2021-02-08 12:16:09.363804
13	Unisex Watches	1000	2021-02-08 12:16:14.112802
14	Men's Joggers	3000	2021-02-08 12:16:24.649859
15	Men's Sweaters	500	2020-02-08 12:16:30.311548
16	Men's T-Shirts	500	2020-02-08 12:16:38.152827
17	Women's T-Shirts	5000	2021-02-08 12:17:01.426941
18	Women's Chelsea Boots	600	2021-02-08 12:15:57.925399
19	Women's Joggers	400	2021-02-08 12:15:57.925399
20	Men's Wool Socks	400	2021-01-08 12:15:57.925399
21	Women's Bomber Jackets	400	2021-02-08 12:15:57.925399
22	Women's Bomber Jackets	600	2021-02-08 12:15:57.925399
23	Women's Bomber Jackets	400	2021-02-08 12:15:57.925399
24	Women's Bomber Jackets	600	2021-02-08 12:15:57.925399
\.


--
-- Name: entries_entry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jnerby
--

SELECT pg_catalog.setval('public.entries_entry_id_seq', 17, true);


--
-- Name: entries entries_pkey; Type: CONSTRAINT; Schema: public; Owner: jnerby
--

ALTER TABLE ONLY public.entries
    ADD CONSTRAINT entries_pkey PRIMARY KEY (entry_id);


--
-- PostgreSQL database dump complete
--

