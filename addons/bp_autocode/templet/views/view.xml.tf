<?xml version="1.0" encoding="utf-8"?>
<odoo>

    % for m in object.module_model_1:
    <!-- 定义form表单视图 -->
     <record id="${m.model_class_name}_form" model="ir.ui.view">
        <field name="name">${m.model_e_name}.form</field>
        <field name="type">form</field>
        <field name="model">${m.model_e_name}</field>
        <field name="arch" type="xml">
            <form>
                <header>
                    % for model_bt in m.model_button:
                    <button class='oe_highlight' type="object" string="${model_bt.button_name}" name="${model_bt.button_method_name}" attrs="{}" />
                    % endfor

                    % if m.is_status == True:
                    <field name="state"  widget="statusbar" statusbar_visible="${','.join(m.show_progress_bar.filtered('progressbar_show').mapped('selection_key'))}" />
                    % endif
                </header>

                <sheet>
                   <div class="oe_button_box" name="button_box">
                            % for model_box in m.model_relatebox:
                            <button name="${model_box.related_method_button}"
                                type="object"
                                icon="fa-pencil-square-o"
                                class="oe_stat_button"
                                help="${model_box.notice_help}">
                                <field name="${model_box.related_field.field_e_name}"  widget="statinfo" string="${model_box.notice_help}"/>
                            </button>
                            % endfor
                   </div>
                      <% set flag = False %>
                     <group>
                      % for model_line in m.model_fieldlines:
                      % if model_line.fields_name.field_type == 'group':
                        % if model_line.beizhu:
                        <group string = "${model_line.beizhu}">
                        % else:
                        <group string = "">
                        % endif
                      % elif model_line.fields_name.field_type == 'groupend':
                        </group>
                      % elif model_line.fields_name.field_type == 'notebook':
                           <%set  flag= True %>
                      % else:
                        % if flag == False:
                        % if model_line.fields_name.field_type not in ['group', 'groupend', 'notebook', 'notebookend', 'page', 'pageend', 'tree', 'treeend']:
                            % if model_line.is_show_form == False:
                        <field name="${model_line.fields_name.field_e_name}" invisible="1"/>
                            % else:
                        <field name="${model_line.fields_name.field_e_name}" />
                            % endif
                        % endif
                      % endif
                     %endif
                     % endfor
                     </group>

                    <% set flag = False %>
                    <% set tree_flag = False %>
                     % for model_line in m.model_fieldlines:
                        % if model_line.fields_name.field_type == 'notebook':
                        <%set  flag= True %>
                        <notebook>
                        % elif flag == True:
                            % if model_line.fields_name.field_type == 'page':
                                % if model_line.beizhu:
                            <page string = "${model_line.beizhu}">
                                % else:
                            <page string="标签页">
                                %endif
                            % elif model_line.fields_name.field_type == 'pageend':

                            </page>
                            % elif model_line.fields_name.field_type == 'group':
                              % if model_line.beizhu:
                                <group string = "${model_line.beizhu}">
                                % else:
                                <group string = "">
                                % endif
                            % elif model_line.fields_name.field_type == 'groupend':
                               <!-- </group>  zpx-->

                            % elif model_line.fields_name.field_type == 'notebookend':
                        </notebook>
                            % elif  model_line.fields_name.field_type == 'tree':
                                <tree editable="bottom">
                                <%set  tree_flag= True %>
                            % elif  model_line.fields_name.field_type == 'treeend':
                                </tree>
                                </field>
                                <%set  tree_flag= False %>
                            % else:
                                % if model_line.fields_name.field_type not in ['group', 'groupend', 'notebook', 'notebookend', 'page', 'pageend', 'tree', 'treeend']:
                                    % if model_line.is_show_form == False:
                            <field name="${model_line.fields_name.field_e_name}" domain="[]" invisible="1"  />

                                    % else:
                                     % if tree_flag == False:
                                        % if model_line.is_show_field_tree == True:
                            <field name="${model_line.fields_name.field_e_name}" domain="[]"  >
                                        % else:
                            <field name="${model_line.fields_name.field_e_name}" domain="[]"  />
                                        % endif
                                     % else:
                            <field name="${model_line.fields_name.field_e_name}"  />
                                     % endif
                                    % endif
                                % endif
                            % endif
                        %endif
                     % endfor

                     % if m.is_upload_file == True:
                     <notebook>
                        <page>
                            <group>
                                <field name="upload_files" mode="kanban">
                                    <kanban create="false" js_class="upload_dashboard">
                                        <field name="dir_name"/>
                                        <field name="file_name"/>
                                        <!--<field name="file_url"/>-->
                                        <field name="data"/>
                                        <field name="table"/>
                                        <field name="file_type"/>
                                        <templates>
                                             <t t-name="kanban-box">
                                        <div>
                                            <a t-if="!read_only_mode" type="delete" class="fa fa-times pull-right"/>
                                            <div class="o_kanban_image">
                                                <img class="dowebok" t-if="record.file_type.raw_value == 'picture'" t-att-id='_s + "/dris_upload/static/file/" + record.dir_name.raw_value + "/preview"' t-att-src='_s + "/dris_upload/static/file/" + record.dir_name.raw_value + "/small"'/>
                                                <t t-if="record.file_type.raw_value == 'file'">
                                                    <i class="i_file_class"/>
                                                </t>
                                                <t t-if="record.file_type.raw_value == 'word'">
                                                    <i class="i_word_class"/>
                                                </t>
                                                <t t-if="record.file_type.raw_value == 'excel'">
                                                    <i class="i_excel_class"/>
                                                </t>
                                                <t t-if="record.file_type.raw_value == 'zip'">
                                                    <i class="i_zip_class"/>
                                                </t>
                                                <t t-if="record.file_type.raw_value == 'pdf'">
                                                    <i class="i_pdf_class"/>
                                                </t>
                                            </div>
                                            <div class="oe_kanban_details">
                                                <strong style="display: block; overflow: hidden;">
                                                    <field name="file_name"/>
                                                </strong>
                                                <div>
                                                    <a t-att-href="'/file_download/'+record.dir_name.raw_value+'/'+record.file_name.raw_value" title="下载" target="_blank">下载</a>
                                                </div>
                                            </div>
                                        </div>
                                    </t>
                                        </templates>
                                    </kanban>
                                </field>

                            </group>
                            <field name="id" class="record_id" invisible="1"/>
                            <templates>
                                <t>
                                    <!--文件信息暂存-->
                                    <div id="upload_files_data" style="display:none;"/>
                                    <div id="uploader" class="wu-example oe_edit_only">
                                        <div class="queueList">
                                            <div id="dndArea" class="placeholder">
                                                <div id="filePicker"></div>
                                            </div>
                                            <div class="statusBar" style="display: none;">
                                                <div class="info"></div>
                                                <div class="btns">
                                                    <div id="filePicker2"></div>
                                                    <div class="uploadBtn">开始上传</div>
                                                </div>
                                            </div>
                                            <p id="getnewnum"></p>
                                        </div>
                                    </div>
                                    <link rel="stylesheet" type="text/css" href="dris_upload/static/webuploader/webuploader.css"/>
                                    <link rel="stylesheet" type="text/css" href="dris_upload/static/index.css"/>
                                    <script type="text/javascript" src="dris_upload/static/webuploader/webuploader.js"/>
                                    <script type="text/javascript" src="dris_upload/static/index.js"/>
                                    <link rel="stylesheet" type="text/css" href="dris_upload/static/preview/css/viewer.min.css"/>
                                    <script type="text/javascript" src="dris_upload/static/preview/js/viewer.min.js"/>
                                </t>
                            </templates>
                        </page>
                    </notebook>
                   % endif

                </sheet>

            <!-- 备注信息轨迹显示 begin-->
                <div class="oe_chatter">
                    <field name="message_follower_ids" widget="mail_followers"/>
                    <field name="message_ids" widget="mail_thread"/>
                </div>
            <!-- 备注信息轨迹显示 end-->

            </form>
        </field>
     </record>

     <!-- 定义tree列表视图 -->
    <record id="${m.model_class_name}_tree" model="ir.ui.view">
        <field name="name">${m.model_e_name}.tree</field>
        <field name="type">tree</field>
        <field name="model">${m.model_e_name}</field>
        <field name="arch" type="xml">
            <tree>
                % for model_line in m.model_fieldlines:
                    % if model_line.fields_name.field_type not in ['group', 'groupend', 'notebook', 'notebookend', 'page', 'pageend', 'tree', 'treeend']:
                        % if model_line.is_show_tree == False:
                <field name="${model_line.fields_name.field_e_name}" string="${model_line.fields_name.field_c_name}" invisible="1"/>
                        % else:
                <field name="${model_line.fields_name.field_e_name}" string="${model_line.fields_name.field_c_name}"/>
                        % endif
                    % endif
                % endfor
            </tree>
        </field>
    </record>

    <!-- 定义筛选器视图 -->
    <record id="${m.model_class_name}_search_view" model="ir.ui.view">
        <field name="name">${m.model_e_name}.search</field>
        <field name="model">${m.model_e_name}</field>
        <field name="arch" type="xml">
            <search string="">
                % for model_line in m.model_fieldlines:
                    % if model_line.fields_name.field_type not in ['group', 'groupend', 'notebook', 'notebookend', 'page', 'pageend', 'tree', 'treeend']:
                        % if model_line.is_filter == True:
                <field name="${model_line.fields_name.field_e_name}" string="${model_line.fields_name.field_c_name}"/>
                        % endif
                    % endif
                % endfor

                % if m.is_screening == True:
                    % for model_filter in m.show_filter:
                        % if model_filter.filter_fields.field_type not in ['group', 'groupend', 'notebook', 'notebookend', 'page', 'pageend', 'tree', 'treeend']:
                <filter  string="${model_filter.filter_name}"  domain="${model_filter.fields_content}" />
                        % endif
                    % endfor
                % endif

                <!-- 定义分组器 -->
                <group expand="0" string="Group By">
                    % for model_line in m.model_fieldlines:
                        % if model_line.fields_name.field_type not in ['group', 'groupend', 'notebook', 'notebookend', 'page', 'pageend', 'tree', 'treeend']:
                            % if model_line.is_group == True:
                    <filter name="${model_line.fields_name.field_e_name}" string="${model_line.fields_name.field_c_name}" domain="[]" context="{'group_by':'${model_line.fields_name.field_e_name}'}"/>
                            % endif
                        %endif
                    % endfor
                </group>
            </search>
        </field>
    </record>
    % if m.is_graph == True:
    <!-- 定义看板视图-->
    <record id="${m.model_class_name}_kanban_view" model="ir.ui.view">
        <field name="name">${m.model_e_name}.kanban</field>
        <field name="type">kanban</field>
        <field name="model">${m.model_e_name}</field>
        <field name="arch" type="xml">
            <kanban class="o_kanban_mobile">
               % for model_line in m.model_fieldlines:
                    % if model_line.fields_name.field_type not in ['group', 'groupend', 'notebook', 'notebookend', 'page', 'pageend', 'tree', 'treeend']:
                        % if m.is_graph == True:
                <field name="${model_line.fields_name.field_e_name}" string="${model_line.fields_name.field_c_name}"/>
                        % endif
                    %endif
                % endfor
               <templates>
                    <t t-name="kanban-box">
                        <div t-attf-class="oe_kanban_card oe_kanban_global_click">
                            % for model_line in m.model_fieldlines:
                                % if model_line.fields_name.field_type not in ['group', 'groupend', 'notebook', 'notebookend', 'page', 'pageend', 'tree', 'treeend']:
                                    % if m.is_graph == True:
                            <div class="row">
                                <div class="col-xs-6 pull-right text-right">
                                    <strong><span>
                                        <t>

                                            <t t-esc="record.${model_line.fields_name.field_e_name}.value"/>
                                        </t>
                                    </span></strong>
                                </div>
                            </div>
                                    % endif
                                %endif
                            % endfor
                        </div>
                    </t>
               </templates>
            </kanban>
        </field>
    </record>

    <!-- 定义日历视图-->
    <!--<record id="${m.model_class_name}_calendar_view" model="ir.ui.view">
        <field name="name">${m.model_e_name}.calendar</field>
        <field name="model">${m.model_e_name}</field>
        <field name="arch" type="xml">
            <calendar string="${m.model_e_name}" color="" date_start="">
                % for model_line in m.model_fieldlines:
                    % if m.is_graph == True:
                <field name="${model_line.fields_name.field_e_name}" />
                    % endif
                % endfor
            </calendar>
        </field>
    </record>-->

    <!-- 定义柱状折线饼状图形视图-->
    <record id="${m.model_class_name}_graph_view" model="ir.ui.view">
        <field name="name">${m.model_e_name}.graph</field>
        <field name="model">${m.model_e_name}</field>
        <field name="arch" type="xml">
            <graph string="${m.model_e_name}">
                % for model_line in m.model_fieldlines:
                    % if model_line.fields_name.field_type not in ['group', 'groupend', 'notebook', 'notebookend', 'page', 'pageend', 'tree', 'treeend']:
                        % if m.is_graph == True:
                <field name="${model_line.fields_name.field_e_name}" type="measure"/>
                        % endif
                    % endif
                % endfor
            </graph>
        </field>
    </record>

    <!-- 定义透视表视图-->
    <record id="${m.model_class_name}_pivot_view" model="ir.ui.view" >
        <field name="name">${m.model_e_name}.pivot</field>
        <field name="model">${m.model_e_name}</field>
        <field name="arch" type="xml">
            <pivot string="${m.model_e_name}" display_quantity="true">
                % for model_line in m.model_fieldlines:
                    % if model_line.fields_name.field_type not in ['group', 'groupend', 'notebook', 'notebookend', 'page', 'pageend', 'tree', 'treeend']:
                        % if m.is_graph == True:
                <field name="${model_line.fields_name.field_e_name}" type="measure"/>
                        % endif
                    % endif
                % endfor
            </pivot>
        </field>
    </record>
    % endif
   <!-- 定义视图动作 -->
     <record id="${m.model_class_name}_action" model="ir.actions.act_window">
        <field name="name">${m.model_description}</field>
        <field name="res_model">${m.model_e_name}</field>
        <field name="type">ir.actions.act_window</field>
        <field name="view_type">form</field>
        % if m.is_graph == True:
        <field name="view_mode">tree,form,kanban,graph,pivot</field>
        % else:
        <field name="view_mode">tree,form</field>
        % endif
         <field name="view_id" ref="${m.model_class_name}_tree"/>
    </record>
    <!-- 触发tree视图动作 -->
    <record model="ir.actions.act_window.view" id="${m.model_class_name}_tree_action">
            <field name="view_mode">tree</field>
            <field name="view_id" ref="${m.model_class_name}_tree"/>
            <field name="sequence">1</field>
            <field name="act_window_id" ref="${m.model_class_name}_action"/>
    </record>
    <!-- 触发form视图动作 -->
    <record model="ir.actions.act_window.view" id="${m.model_class_name}_form_action">
            <field name="view_mode">form</field>
            <field name="view_id" ref="${m.model_class_name}_form"/>
            <field name="sequence">2</field>
            <field name="act_window_id" ref="${m.model_class_name}_action"/>
    </record>
    % endfor


    <menuitem id="menu_top" name="${object.module_c_name}" />
    % for m in object.module_model_1
    <menuitem id="${m.model_class_name}_menu_field"   name="${m.model_description}" parent="menu_top" sequence="14" action="${m.model_class_name}_action"/>
    % endfor
</odoo>

