update callingtreexcallingtree set
 callingtreexcallingtree_author = <dtml-sqlvar expr="aq_inner.username()" type="string">,
 callingtreexcallingtree_modtime = now(),
 callingtreexcallingtree_parent_id = <dtml-var expr="sql_int(parent_id)">,
 callingtreexcallingtree_child_id = <dtml-var expr="sql_int(child_id)">,
 callingtreexcallingtree_acquisition = <dtml-var expr="sql_string(acquisition)">

<dtml-sqlgroup where>
 callingtreexcallingtree_id = <dtml-sqlvar id type="int">::bigint  
<dtml-and>
 <dtml-var expr="db_selfilter_sql('callingtreexcallingtree', 'callingtreexcallingtree_id')">
</dtml-sqlgroup>
