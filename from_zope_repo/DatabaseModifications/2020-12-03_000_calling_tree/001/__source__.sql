CREATE TABLE IF NOT EXISTS public.callingtree (
    callingtree_id bigint NOT NULL,
    callingtree_modtime timestamp with time zone DEFAULT now() NOT NULL,
    callingtree_author character varying(80),
    callingtree_path character varying(255) NOT NULL,
    callingtree_filename character varying(255) NOT NULL,
    callingtree_callingtreetype_id integer NOT NULL,
    callingtree_filemodded timestamp with time zone,
    callingtree_fileparsed timestamp with time zone,
    callingtree_functionlist text[],
    callingtree_scanned boolean DEFAULT false NOT NULL
);

ALTER TABLE public.callingtree OWNER TO zope;

COMMENT ON COLUMN public.callingtree.callingtree_id IS 'Graphknoten des Funktionsaufrufbaums';
COMMENT ON COLUMN public.callingtree.callingtree_path IS 'Physischer Pfad des Zope-Objekts';
COMMENT ON COLUMN public.callingtree.callingtree_filename IS 'Name des Zope-Objekts';
COMMENT ON COLUMN public.callingtree.callingtree_callingtreetype_id IS 'Interpretationstyp';
COMMENT ON COLUMN public.callingtree.callingtree_filemodded IS 'Änderungsdatum der Datei';
COMMENT ON COLUMN public.callingtree.callingtree_fileparsed IS 'Änderungsdatum der Datei, welche zuletzt geparst wurde';
COMMENT ON COLUMN public.callingtree.callingtree_functionlist IS 'Liste der aufgerufenen Funktionen';
COMMENT ON COLUMN public.callingtree.callingtree_scanned IS 'Hilfsattribut zum Ermitteln gelöschter Knoten beim erneuten Scan.';

CREATE SEQUENCE IF NOT EXISTS public.callingtree_s
    START WITH 1001
    INCREMENT BY 1
    MINVALUE 1001
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.callingtree_s OWNER TO zope;

ALTER SEQUENCE public.callingtree_s OWNED BY public.callingtree.callingtree_id;

ALTER TABLE ONLY public.callingtree ALTER COLUMN callingtree_id SET DEFAULT nextval('public.callingtree_s'::regclass);

ALTER TABLE ONLY public.callingtree
    DROP CONSTRAINT IF EXISTS callingtree_pkey CASCADE;

ALTER TABLE ONLY public.callingtree
    ADD CONSTRAINT callingtree_pkey PRIMARY KEY (callingtree_id);

CREATE UNIQUE INDEX IF NOT EXISTS callingtree_path_filename ON public.callingtree USING btree (callingtree_path, callingtree_filename);

ALTER TABLE ONLY public.callingtree 
    DROP CONSTRAINT IF EXISTS callingtreetype_id;

ALTER TABLE ONLY public.callingtree
    ADD CONSTRAINT callingtreetype_id FOREIGN KEY (callingtree_callingtreetype_id) REFERENCES public.callingtreetype(callingtreetype_id) ON UPDATE CASCADE ON DELETE CASCADE;






