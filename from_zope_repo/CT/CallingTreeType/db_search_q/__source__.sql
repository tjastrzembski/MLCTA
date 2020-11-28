select
 callingtreetype_id,
 callingtreetype_modtime,
 callingtreetype_desc,
 callingtreetype_parseable

from
 callingtreetype
 

<dtml-sqlgroup where>
  <dtml-var db_search_sql>  
<dtml-and>
 <dtml-var expr="db_selfilter_sql('callingtreetype', 'callingtreetype_id')">
</dtml-sqlgroup>

<dtml-var db_sort_sql>

limit <dtml-var db_search_limit>
