select
 callingtreexcallingtree_id,
 callingtreexcallingtree_parent_id,
 callingtreexcallingtree_child_id,
 callingtreexcallingtree_acquisition::text

from
 callingtreexcallingtree
 

<dtml-sqlgroup where>
  <dtml-var db_search_sql>  
<dtml-and>
 <dtml-var expr="db_selfilter_sql('callingtreexcallingtree', 'callingtreexcallingtree_id')">
</dtml-sqlgroup>

<dtml-var db_sort_sql>

limit <dtml-var db_search_limit>
