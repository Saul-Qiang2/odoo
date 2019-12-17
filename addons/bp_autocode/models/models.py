# -*- coding: utf-8 -*-
import os, re
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools import config

class BPAutocodeModule(models.Model):

    _name = 'bp_autocode.module'
    _description = u'模块'
    _rec_name = 'module_c_name'
    module_c_name = fields.Char(string="模块中文名称", required=True)
    module_e_name = fields.Char(string="模块英文名称", required=True)
    module_model_1 = fields.Many2many("bp_autocode.model", string="模型详情框")
    rely_module = fields.Many2many("bp_autocode.module.rely.module", string=u'所依赖的模块')
    show_module = fields.One2many('bp_autocode.module.rely.module', 'rely_module_id', string=u'依赖模块信息表')
    raw_inherit_model = fields.One2many('bp_autocode.inherit.field', 'inherit_field_id', string=u'原生模型')

    @api.constrains('module_e_name')
    def remove_trim_module_e_name(self):
        filter_is_null(self.module_e_name)

    @api.onchange("rely_module")
    def create_rely_module(self):
        res = []
        for mu in self.rely_module:
            res.append({
                "rely_module_cname": mu.rely_module_cname,
                "rely_module_ename": mu.rely_module_ename,
            })
        self.show_module = res

    @api.multi
    def create_code(self):
        # auto_code_path = 'D:/Work/dvt/odoo-10.0-hbgj/addons/bp_autocode/templet/'  # 自动生成代码模板路径(手动维护)
        # config['addons_path']
        print(config['addons_path'].split(',')[1] + '/' + 'bp_autocode' + '/' + 'templet' + '/')
        # auto_code_path = self.code_path  # 自动生成代码模板路径(手动维护)
        auto_code_path = config['addons_path'].split(',')[1] + '/' + 'bp_autocode' + '/' + 'templet' + '/'  # 自动生成代码模板路径(手动维护)
        module_path = config['addons_path'].split(',')[1] + '/' + self.module_e_name  # 生成的模块路径

        self.os_mkdir(module_path)
        self.os_mkdir(module_path + '/' + 'models')
        self.os_mkdir(module_path + '/' + 'views')
        self.os_mkdir(module_path + '/' + 'security')


        self.readtfFile(auto_code_path + "__init__.py.tf", module_path + '/' + "__init__.py", self, self.id)
        self.readtfFile(auto_code_path + "__manifest__.py.tf", module_path + '/' + "__manifest__.py", self, self.id)
        self.readtfFile(auto_code_path + "models/__init__.py.tf", module_path + '/' + "models/__init__.py", self, self.id)
        self.readtfFile(auto_code_path + "security/ir.model.access.csv.tf", module_path + '/' + "security/ir.model.access.csv", self, self.id)

        if self.module_model_1:
            self.readtfFile(auto_code_path + "models/model.py.tf",
                            module_path + '/' + "models/" + "model.py", self, self.id)
            self.readtfFile(auto_code_path + "views/view.xml.tf",
                            module_path + '/' + "views/" + "view.xml", self, self.id)
        if self.raw_inherit_model:
            self.readtfFile(auto_code_path + "models/inh_model.py.tf",
                            module_path + '/' + "models/" + "inh_model.py", self, self.id)
            self.readtfFile(auto_code_path + "views/inh_view.xml.tf",
                            module_path + '/' + "views/" + "inh_view.xml", self, self.id)


        # for m in self.module_model_1:
            # self.readtfFile(auto_code_path + "models/model.py.tf", module_path + '/' + "models/" + m.model_class_name + "_model.py", m, m.id)
            # self.readtfFile(auto_code_path + "views/view.xml.tf", module_path + '/' + "views/" + m.model_class_name + "_view.xml", m, m.id)

        # for raw_m in self.raw_inherit_model:
            # self.readtfFile(auto_code_path + "models/inh_model.py.tf",
            #                 module_path + '/' + "models/" + raw_m.ref_inh_class_name + "_inh_model.py", raw_m, raw_m.id)
            # self.readtfFile(auto_code_path + "views/inh_view.xml.tf",
            #                 module_path + '/' + "views/" + raw_m.ref_inh_class_name + "_inh_view.xml", raw_m, raw_m.id)

    def readtfFile(self, fileName, codeFileName, obj, id):
        def _callback(matches):
            id = matches.group(1)
            try:
                return unichr(int(id))
            except:
                return id
        # if os.path.exists(codeFileName):
        #     return print('该文件已存在')
        file = open(fileName, "r", encoding="utf-8")
        codeFile = open(codeFileName, "w", encoding="utf-8")
        subjectCode = " "
        for line in file:
            subjectCode = subjectCode + line
        mailTemplate = self.env['mail.template']
        print(id)
        generated_field_values = mailTemplate._render_template(subjectCode, obj._name, id)

        templet = generated_field_values
        templet = templet.strip()
        templet = re.sub("&#(\d+)(;|(?=\s))", _callback, templet)
        codeFile.write(templet)
        file.close()
        codeFile.close()
        print('生成文件', codeFileName)

    def os_mkdir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
        return True

class AutoCodeModuleRelyModule(models.Model):
    _name = 'bp_autocode.module.rely.module'
    _description = u'模块依赖模块表'
    _rec_name = 'rely_module_cname'
    rely_module_id = fields.Many2one('bp_autocode.module', string=u'请选择模块')
    rely_module_cname = fields.Char(string=u'依赖模块的中文名称')
    rely_module_ename = fields.Char(string=u'依赖模块的英文名称')

class AutoCodeAddelField(models.Model):
    # 增减原生字段信息继承类
    _name = 'bp_autocode.addel.field'
    _rec_name = 'raw_table_model'
    _description = u'增减原生字段信息表'

    # 模型类名
    inh_class_name = fields.Char(string=u'继承模型的类名', required=True)
    # 继承某个模型(给某个模型加字段)
    raw_table_model = fields.Many2one('ir.model', string=u'请选择原生模型', required=True)
    # 加某个字段（用自己auto的表）
    auto_field_name = fields.Many2many('bp_autocode.field', string=u'请选择添加字段')
    # 加到哪个View页面
    raw_view_id = fields.Many2one('ir.ui.view', string=u'请选择继承的目标视图', required=True)
    # 加到哪个原生字段
    raw_field_name = fields.Many2one('ir.model.fields', string=u'请选择继承的原生字段')
    # Record唯一ID
    record_view_id = fields.Char(string=u'Record视图唯一ID', required=True)
    choose_module = fields.Many2one('bp_autocode.module.rely.module', string=u'选择模块')
    # Position位置
    # position_type = fields.Selection([('before', 'before'), ('after', 'after'), ('inside', 'inside'), ('attributes', 'attributes'), ('replace', 'replace')], string=u'Position类型', required=True)
    position_type = fields.Selection([('before', 'before'), ('after', 'after'), ('replace', 'replace')], string=u'Position类型', required=True)
    expr_type = fields.Selection([('field', 'field'), ('button', 'button')], string=u'Expr类型', required=True)
    button_field = fields.Char(string=u'原生Button方法名')
    button_new_filed = fields.Many2many('bp_autocode.model.button', string=u'请选择button名称')
    raw_hidden_field_name = fields.Many2many('ir.model.fields', string=u'请选择要隐藏的原生字段')

    @api.constrains('inh_class_name', 'record_view_id')
    def remove_trim_inh_class_name_record_view_id(self):
        # for str in self.inh_class_name:
        #     if str.isspace():
        #         raise ValidationError(u"继承模型类名中不允许出现空格!")
        # for str in self.record_view_id:
        #     if str.isspace():
        #         raise ValidationError(u"视图RecordID中不允许出现空格!")
        filter_is_null(self.inh_class_name)
        filter_is_null(self.record_view_id)

    # ('record_view_id')
    # def remove_trim_record_view_id(self):
    #     for str in self.record_view_id:
    #         if str.isspace():
    #             raise ValidationError(u"视图RecordID中不允许出现空格!")

class AutoCodeInheritField(models.Model):
    # 继承表扩展表
    _name = 'bp_autocode.inherit.field'
    # _rec_name = ''
    _description = u'增减原生字段扩展信息表'

    inherit_field_id = fields.Many2one('bp_autocode.module', string=u'关联模块')
    addel_field_id = fields.Many2one('bp_autocode.addel.field', string=u'原生被继承模型')
    ref_inh_class_name = fields.Char(related='addel_field_id.inh_class_name', string=u'继承模型的类名')
    ref_auto_field_name = fields.Many2many(related='addel_field_id.auto_field_name', string=u'添加的新字段')
    ref_raw_view_id = fields.Many2one(related='addel_field_id.raw_view_id', string=u'继承的目标视图ID')
    ref_raw_field_name = fields.Many2one(related='addel_field_id.raw_field_name', string=u'原生被继承字段', readonly="1")
    ref_raw_hidden_field_name = fields.Many2many(related='addel_field_id.raw_hidden_field_name', string=u'原生要隐藏的字段')
    ref_record_view_id = fields.Char(related='addel_field_id.record_view_id', string=u'Record视图唯一ID')
    ref_position_type = fields.Selection(related='addel_field_id.position_type', string=u'Position类型')
    ref_expr_type = fields.Selection(related='addel_field_id.expr_type', string=u'Expr类型')
    ref_button_field = fields.Char(related='addel_field_id.button_field', string=u'原生Button方法名')
    ref_button_new_filed = fields.Many2many(related='addel_field_id.button_new_filed', string=u'请选择button名称', readonly="1")
    hidden_raw_field = fields.Boolean(string=u'是否隐藏')

    # @api.depends('addel_field_id.inh_class_name')
    # def _compute_ref_inh_class_name(self):
    #     self.ref_inh_class_name = self.addel_field_id.inh_class_name

    # @api.depends('addel_field_id.raw_field_name')
    # def _compute_ref_raw_field_name(self):
    #     self.ref_raw_field_name = self.addel_field_id.raw_field_name.field_description

    # @api.depends('addel_field_id.auto_field_name')
    # def _compute_ref_auto_field_name(self):
    #     self.ref_auto_field_name = self.addel_field_id.auto_field_name

    # @api.depends('addel_field_id.raw_view_id')
    # def _compute_ref_raw_view_id(self):
    #     self.ref_raw_view_id = self.addel_field_id.raw_view_id.name

    # @api.multi
    # @api.depends('addel_field_id.raw_hidden_field_name')
    # def _compute_ref_raw_hidden_field_name(self):
    #     for r in self.addel_field_id.raw_hidden_field_name:
    #         self.ref_raw_hidden_field_name = r.field_description
    #         break
    #     self.ref_raw_hidden_field_name = self.ref_raw_hidden_field_name

class BPAutocodeModel(models.Model):
    _name = 'bp_autocode.model'
    _description = u'模型'
    _rec_name = 'model_e_name'
    model_e_name = fields.Char(string="模型英文名称(表名)", required=True)

    model_class_name = fields.Char(string="模型对应的类名称", required=True)
    model_description = fields.Char(string="模型描述", required=True)
    is_graph = fields.Boolean(string=u'是否展示图表')
    model_button = fields.Many2many("bp_autocode.model.button", string=u'创建按钮')
    is_status = fields.Boolean(string=u'是否显示状态进度条')
    show_progress_bar = fields.One2many('bp_autocode.model.progressbar', 'progressbar_id', string=u'模型进度条信息表')
    is_screening = fields.Boolean(string=u'是否显示筛选器')
    show_filter = fields.One2many('bp_autocode.model.filter', 'filter_id', string=u'模型筛选器信息表')
    model_fieldlines = fields.One2many('bp_autocode.model.fieldline', 'model_id', string=u'字段列表')
    model_relatebox = fields.Many2many('bp_autocode.model.relatedbox', string=u'创建关联框')

    show_button = fields.One2many('bp_autocode.model.button', 'button_id', string=u'模型按钮信息表')
    show_relatedbox = fields.One2many('bp_autocode.model.relatedbox', 'relatedbox_id', string=u'模型关联框信息表')
    model_e_name_underline = {}


    def create_model_e_name_underline(self):
        print(type(self.model_e_name))
        if self.model_e_name:
            # self.model_e_name_underline[self.model_e_name] = self.model_e_name.replace('.', '_')
            return self.model_e_name.replace('.', '_')



    @api.constrains('model_e_name', 'model_class_name')
    def remove_trim_name_class_name(self):
        filter_is_null(self.model_e_name)
        filter_is_null(self.model_class_name)

    @api.onchange("model_button")
    def create_model_button(self):
        res = []
        for button_one in self.model_button:
            res.append({
                "button_name": button_one.button_name,
                "button_method_name": button_one.button_method_name
            })
        self.show_button = res

    @api.onchange("model_relatebox")
    def create_model_relatebox(self):
        res = []
        for box in self.model_relatebox:
            res.append({
                "related_field": box.related_field,
                "related_method_button": box.related_method_button,
                "notice_help": box.notice_help,
            })
        self.show_relatedbox = res

class ModelFieldLine(models.Model):
    _name = 'bp_autocode.model.fieldline'
    # _rec_name = 'fields_name'
    _description = u'模型字段行表信息'
    _order = 'sequence'

    sequence = fields.Integer(string='Sequence', default=10)
    fields_name = fields.Many2one('bp_autocode.field', string=u'字段选择', required=True, ondelete='cascade')
    model_id = fields.Many2one('bp_autocode.model', string=u'模型')
    is_filter = fields.Boolean(string=u'是否筛选')
    is_group = fields.Boolean(string=u'是否分组')
    is_required = fields.Boolean(string=u'是否必填')
    is_readonly = fields.Boolean(string=u'是否只读')
    is_show_form = fields.Boolean(string=u'Form视图是否显示', default=True)
    is_show_tree = fields.Boolean(string=u'Tree视图是否显示', default=True)
    tracking_info = fields.Selection([('onchange', 'onchange'), ('always', 'always')], string=u'追踪信息显示', default='onchange')
    fields_type = fields.Selection(related='fields_name.field_type', string=u'字段类型', readonly=True)
    fields_related_model = fields.Char(related='fields_name.field_related_model', string=u'字段关联模型', readonly=True)
    fields_one_2_many = fields.Char(related='fields_name.field_one_2_many', string=u'关联字段', readonly=True)
    fields_selection = fields.Char(related='fields_name.field_selection', string=u'Selection字段表达式', readonly=True)
    beizhu = fields.Char(string=u'Group备注信息')
    is_show_field_tree = fields.Boolean(string=u'是否展示为tree编辑框')
    fields_e_name = fields.Char(related='fields_name.field_e_name', string=u'字段英文名', readonly=True)

    @api.onchange('is_required')
    def _onchange_is_required(self):
        self.update({'is_readonly': False})

    @api.onchange('is_readonly')
    def _onchange_is_readonly(self):
        self.update({'is_required': False})

class ModelFilter(models.Model):
    _name = 'bp_autocode.model.filter'
    _description = u'模型筛选器信息表'

    filter_id = fields.Many2one('bp_autocode.model', string=u'模型')
    filter_name = fields.Char(string=u'筛选器中文显示名称', required=True)
    filter_regex = fields.Selection([('=', '='), ('!=', '!='), ('in', 'in'), ('not in', 'not in')], string=u'筛选规则')
    filter_fields = fields.Many2one('bp_autocode.field', string=u'字段选择')
    fields_content = fields.Char(string=u'Domain过滤表达式')
    filter_method_name = fields.Char(string=u'筛选器触发的方法名')

class ModelButton(models.Model):
    _name = 'bp_autocode.model.button'
    _rec_name = 'button_name'
    _description = u'模型按钮信息表'

    button_id = fields.Many2one('bp_autocode.model', string=u'请选择模型')
    button_name = fields.Char(string=u'按钮中文显示名称')
    button_method_name = fields.Char(string=u'按钮触发的方法名')

class ModelRelatebox(models.Model):
    _name = 'bp_autocode.model.relatedbox'
    _rec_name = 'notice_help'
    _description = u'模型关联框信息表'

    relatedbox_id = fields.Many2one('bp_autocode.model', string=u'请选择模型')
    related_field = fields.Many2one('bp_autocode.field', string=u'关联的字段')
    related_method_button = fields.Char(string=u'按钮的方法名')
    notice_help = fields.Char(string=u'help提示信息')

class ModelProgressBar(models.Model):
    _name = 'bp_autocode.model.progressbar'
    _description = u'模型进度条信息表'
    _order = 'sequence'

    sequence = fields.Integer(string='Sequence', default=1)
    progressbar_id = fields.Many2one('bp_autocode.model', string=u'请选择模型')
    selection_key = fields.Char(string=u'Selection的key', required=True)
    selection_value = fields.Char(string=u'Selection的value', required=True)
    progressbar_show = fields.Boolean(string=u'是否显示', default=True)

class BPAutocodeField(models.Model):

    _name = 'bp_autocode.field'
    _description = u'字段'
    _rec_name = 'field_c_name'
    field_c_name = fields.Char(string="字段中文名称", required=True)
    field_e_name = fields.Char(string="字段英文名称", required=True)
    field_type = fields.Selection([('Char', u'Char'), ('Integer', u'Integer'), ('Float', u'Float'), ('Boolean', u'Boolean'),
                              ('Selection', u'Selection'), ('Date', u'Date'), ('Datetime', u'Datetime'),
                              ('Text', u'Text'), ('Serialized', u'Serialized'), ('Many2one', u'Many2one'), ('Monetary', 'Monetary'), ('Reference', u'Reference'),
                              ('Many2many', u'Many2many'), ('One2many', u'One2many'), ('Binary', u'Binary'), ('Html', 'Html'), ('group', u'group'), ('groupend', u'groupend'),
                                ('notebook', u'notebook'), ('notebookend', u'notebookend'), ('page', u'page'), ('pageend', u'pageend'), ('tree', u'tree'), ('treeend', u'treeend')],
                                string=u'字段类型', readonly=False, required=True, translate=False)

    field_related_model = fields.Char(string=u'关联模型')
    field_one_2_many = fields.Char(string=u'关联字段')
    field_selection = fields.Char(string=u'Selection字段表达式')

    @api.constrains('field_e_name', 'field_related_model', 'field_one_2_many')
    def remove_trim_e_name_related_model_one_2_many(self):
        filter_is_null(self.field_e_name)
        filter_is_null(self.field_related_model)
        filter_is_null(self.field_one_2_many)

def filter_is_null(field):
    if field:
        for str in field:
            if str.isspace():
                raise ValidationError(u"字段中不允许出现空格!")