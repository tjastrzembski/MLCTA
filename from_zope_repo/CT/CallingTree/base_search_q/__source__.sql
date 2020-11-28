select
 callingtree_id,
 callingtree_path,
 callingtree_filename,
 (select callingtreetype_desc from callingtreetype where callingtreetype_id = callingtree_callingtreetype_id) as lookup_callingtree_callingtreetype_id,
 callingtree_filemodded,
 callingtree_fileparsed,
 callingtree_functionlist::text
from
 callingtree
 

 

<dtml-sqlgroup where>
  <dtml-var db_search_sql>  
<dtml-and>
 <dtml-var expr="db_selfilter_sql('callingtree', 'callingtree_id')">
</dtml-sqlgroup>

<dtml-var db_sort_sql>