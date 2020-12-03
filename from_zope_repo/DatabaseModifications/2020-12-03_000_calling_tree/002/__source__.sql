CREATE TABLE IF NOT EXISTS public.callingtreexcallingtree (
    callingtreexcallingtree_id bigint NOT NULL,
    callingtreexcallingtree_modtime timestamp with time zone DEFAULT now() NOT NULL,
    callingtreexcallingtree_author character varying(80),
    callingtreexcallingtree_parent_id bigint NOT NULL,
    callingtreexcallingtree_child_id bigint NOT NULL,
    callingtreexcallingtree_acquisition text[]
);

ALTER TABLE public.callingtreexcallingtree OWNER TO zope;

COMMENT ON COLUMN public.callingtreexcallingtree.callingtreexcallingtree_parent_id IS 'Aufrufender Graphknoten';
COMMENT ON COLUMN public.callingtreexcallingtree.callingtreexcallingtree_child_id IS 'Aufgerufener Graphknoten';
COMMENT ON COLUMN public.callingtreexcallingtree.callingtreexcallingtree_acquisition IS 'Acquisepfade von aufrufenden Knoten';

CREATE SEQUENCE IF NOT EXISTS public.callingtreexcallingtree_s
    START WITH 1001
    INCREMENT BY 1
    MINVALUE 1001
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.callingtreexcallingtree_s OWNER TO zope;

ALTER SEQUENCE public.callingtreexcallingtree_s OWNED BY public.callingtreexcallingtree.callingtreexcallingtree_id;

ALTER TABLE ONLY public.callingtreexcallingtree ALTER COLUMN callingtreexcallingtree_id SET DEFAULT nextval('public.callingtreexcallingtree_s'::regclass);

ALTER TABLE ONLY public.callingtreexcallingtree
DROP CONSTRAINT IF EXISTS callingtreexcallingtree_pkey CASCADE;

ALTER TABLE ONLY public.callingtreexcallingtree
    ADD CONSTRAINT callingtreexcallingtree_pkey PRIMARY KEY (callingtreexcallingtree_id);

CREATE INDEX IF NOT EXISTS callingtreexcallingtree_child_id ON public.callingtreexcallingtree USING btree (callingtreexcallingtree_child_id);

CREATE INDEX IF NOT EXISTS callingtreexcallingtree_parent_id ON public.callingtreexcallingtree USING btree (callingtreexcallingtree_parent_id);

CREATE UNIQUE INDEX IF NOT EXISTS callingtreexcallingtree_parent_id_child_id ON public.callingtreexcallingtree USING btree (callingtreexcallingtree_parent_id, callingtreexcallingtree_child_id);

ALTER TABLE ONLY public.callingtreexcallingtree
DROP CONSTRAINT IF EXISTS child_id;

ALTER TABLE ONLY public.callingtreexcallingtree
    ADD CONSTRAINT child_id FOREIGN KEY (callingtreexcallingtree_parent_id) REFERENCES public.callingtree(callingtree_id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY public.callingtreexcallingtree
DROP CONSTRAINT IF EXISTS parent_id;

ALTER TABLE ONLY public.callingtreexcallingtree
    ADD CONSTRAINT parent_id FOREIGN KEY (callingtreexcallingtree_parent_id) REFERENCES public.callingtree(callingtree_id) ON UPDATE CASCADE ON DELETE CASCADE;

