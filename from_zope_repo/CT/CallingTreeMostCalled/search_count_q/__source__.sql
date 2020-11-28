select 
  coalesce(lookup_callingtree_callingtreetype_id,'Total') as caption,
  count(lookup_callingtree_callingtreetype_id) as count

from(
  <dtml-var expr="base_search_q(src__=1)">
) search_result

group by grouping sets (
    (lookup_callingtree_callingtreetype_id),
    ()
)