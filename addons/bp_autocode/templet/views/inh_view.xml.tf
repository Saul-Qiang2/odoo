<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>
        <!-- 继承视图 -->
        % for raw_m in object.raw_inherit_model:
        <record id="inherit_${object.ref_record_view_id}" model="ir.ui.view">
            <field name="name">${raw_m.ref_raw_view_id.name}</field>
            <field name="model">${raw_m.addel_field_id.raw_table_model.model}</field>
            <field name="inherit_id" ref="${raw_m.ref_raw_view_id.xml_id}"/>
            <field name="arch" type="xml">
                % if raw_m.ref_expr_type == 'field':
                    % if raw_m.ref_position_type == 'replace':
                        % for raw_hidden_fields in raw_m.ref_raw_hidden_field_name:
                <xpath expr="//field[@name='${raw_hidden_fields.name}']" position="replace">
                     <field name="${raw_hidden_fields.name}" invisible="1"/>
                </xpath>
                        % endfor
                    % else:
                <xpath expr="//field[@name='${raw_m.ref_raw_field_name.name}']" position="${raw_m.ref_position_type}">
                     % for inh_fields in raw_m.ref_auto_field_name:
                     <field name="${inh_fields.field_e_name}" string="${inh_fields.field_c_name}"/>
                     % endfor
                </xpath>
                    % endif
                % endif
                % if raw_m.ref_expr_type == 'button':
                <xpath expr="//button[@name='${raw_m.ref_button_filed}']" position="${raw_m.ref_position_type}">
                    % for inh_button in raw_m.ref_button_new_filed:
                    <button name="${inh_button.button_method_name}" type="object"  string="${inh_button.button_name}" />
                    % endfor
                </xpath>
                % endif
            </field>
        </record>
        % endfor
    </data>
</odoo>