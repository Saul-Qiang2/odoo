id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
% for m in object.module_model_1
access_${m.create_model_e_name_underline()},${m.model_e_name},model_${m.create_model_e_name_underline()},,1,1,1,1
% endfor