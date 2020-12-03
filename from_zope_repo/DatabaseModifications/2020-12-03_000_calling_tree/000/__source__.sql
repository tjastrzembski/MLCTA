CREATE TABLE IF NOT EXISTS public.callingtreetype (
    callingtreetype_id bigint NOT NULL,
    callingtreetype_modtime timestamp with time zone DEFAULT now() NOT NULL,
    callingtreetype_author character varying(80),
    callingtreetype_desc character varying(255) NOT NULL,
    callingtreetype_parseable boolean DEFAULT false NOT NULL
);

ALTER TABLE public.callingtreetype OWNER TO zope;

CREATE SEQUENCE IF NOT EXISTS public.callingtreetype_s
    START WITH 1001
    INCREMENT BY 1
    MINVALUE 1001
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.callingtreetype_s OWNER TO zope;

ALTER SEQUENCE public.callingtreetype_s OWNED BY public.callingtreetype.callingtreetype_id;

ALTER TABLE ONLY public.callingtreetype 
ALTER COLUMN callingtreetype_id SET DEFAULT nextval('public.callingtreetype_s'::regclass);

INSERT INTO public.callingtreetype (
    callingtreetype_id, 
    callingtreetype_author, 
    callingtreetype_desc, 
    callingtreetype_parseable
) VAlUES 
(1001,'perfact','Script (Python)',	true),
(1002,'perfact','Z SQL Method',	true),
(1003,'perfact','Page Template',	true),
(1005,'perfact','File(text/html)',	true),
(1007,'perfact','File(text/sql)',	true),
(1008,'perfact','DTML Method',	true),
(1009,'perfact','DTML Document',	true),
(1010,'perfact','Page Template(text/html)',	true),
(1011,'perfact','Page Template(text/xml)',	true),
(1013,'perfact','File(text/javascriptrue)',	false),
(1014,'perfact','File(text/css)',	false)
ON CONFLICT DO NOTHING;

ALTER TABLE ONLY public.callingtreetype
   DROP CONSTRAINT IF EXISTS callingtreetype_pkey CASCADE;

ALTER TABLE ONLY public.callingtreetype
    ADD CONSTRAINT callingtreetype_pkey PRIMARY KEY (callingtreetype_id);

CREATE UNIQUE INDEX IF NOT EXISTS callingtreetype_desc ON public.callingtreetype USING btree (callingtreetype_desc);


