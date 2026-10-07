ALTER TABLE public.subjects
ADD COLUMN IF NOT EXISTS section text NOT NULL DEFAULT '';

NOTIFY pgrst, 'reload schema';
