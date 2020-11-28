<dtml-let test="DTML.method_dtml_let()" 
          test2="DTML" 
          test3="test2.method_dtml_let_generic()"
          test4="getattr(test2,'method_dtml_let_generic_getattr')()">
select 
  now() as actual_datetime,
  <dtml-var username_var> as username,
  <dtml-sqlvar username_sqlvar type="string"> as username2,
  
  <dtml-var expr="username_expr_var()"> as username3,
  <dtml-sqlvar expr="username_expr_sqlvar()" type="string"> as username4,
  
  <dtml-sqlvar test type="string"> as test,
  <dtml-sqlvar test3 type="string"> as test3
  
  <dtml-if expr="DTML.method_dtml_if()">
      ,<dtml-sqlvar test4 type="string"> as test4
  </dtml-if>
  
  <dtml-in expr="DTML.method_dtml_in()" mapping>
  ,<dtml-sqlvar name type="string"> as <dtml-var name>
  </dtml-in>
  
</dtml-let>