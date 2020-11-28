select 
  count(*) filter (where callingtree_fileparsed is not null) as count

from(
  <dtml-var expr="base_search_q(src__=1)">
) search_result