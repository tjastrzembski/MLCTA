select
 callingtree_id,
 callingtree_path,
 callingtree_filename,
 callingtree_callingtreetype_id,
 (select name from callingtreetype_sel where id = callingtree_callingtreetype_id) as lookup_callingtree_callingtreetype_id,
 callingtreexcallingtree_acquisition,
 callingtree_id as "callingtree_id|xrefgoto"

from
 callingtree
 
join callingtreexcallingtree
  on callingtreexcallingtree_child_id = callingtree_id
 

<dtml-sqlgroup where>
  <dtml-var db_search_sql>  
<dtml-and>
 <dtml-var expr="db_selfilter_sql('callingtree', 'callingtree_id')">
</dtml-sqlgroup>

<dtml-var db_sort_sql>

limit <dtml-var db_search_limit>
