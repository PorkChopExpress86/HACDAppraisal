import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class BuildingRes(db.Model):
    __tablename__ = 'building_res'

    index = db.Column(db.BigInteger, primary_key=True)
    acct = db.Column(db.BigInteger)
    property_use_cs = db.Column(db.Text)
    bld_num = db.Column(db.BigInteger, nullable=False)
    impr_tp = db.Column(db.BigInteger)
    impr_mdl_cd = db.Column(db.BigInteger)
    structure = db.Column(db.Text)
    structure_dscr = db.Column(db.Text)
    dpr_val = db.Column(db.Text)
    cama_replacement_cost = db.Column(db.Text)
    accrued_depr_pct = db.Column(db.Float)
    qa_cd = db.Column(db.Text)
    dscr = db.Column(db.Text, nullable=False)
    date_erected = db.Column(db.BigInteger)
    eff = db.Column(db.BigInteger)
    yr_remodel = db.Column(db.BigInteger)
    yr_roll = db.Column(db.Text)
    appr_by = db.Column(db.Text)
    appr_dt = db.Column(db.Text)  # is a date in MM/DD/YYYY format
    notes = db.Column(db.Text)
    im_sq_ft = db.Column(db.BigInteger)
    act_ar = db.Column(db.BigInteger)
    heat_ar = db.Column(db.BigInteger)
    gross_ar = db.Column(db.BigInteger)
    eff_ar = db.Column(db.BigInteger)
    base_ar = db.Column(db.BigInteger)
    perimeter = db.Column(db.BigInteger)
    pct = db.Column(db.Float)
    bld_adj = db.Column(db.Float)
    rcnld = db.Column(db.Float)
    size_index = db.Column(db.Float)
    lump_sum_adj = db.Column(db.BigInteger)


class Lands(db.Model):
    __tablename__ = 'land'

    index = db.Column(db.BigInteger, primary_key=True)
    acct = db.Column(db.BigInteger)
    num = db.Column(db.BigInteger)
    use_cd = db.Column(db.BigInteger)
    use_dscr = db.Column(db.Text)
    inf_cd = db.Column(db.Text)
    inf_dscr = db.Column(db.Text)
    inf_adj = db.Column(db.Float)
    tp = db.Column(db.Text)
    uts = db.Column(db.Float)
    sz_fact = db.Column(db.Float)
    inf_fact = db.Column(db.Float)
    cond = db.Column(db.Float)
    ovr_dscr = db.Column(db.Text)
    tot_adj = db.Column(db.Float)
    unit_prc = db.Column(db.Text)
    adj_unit_prc = db.Column(db.Text)
    val = db.Column(db.Text)
    ovr_val = db.Column(db.Text)


class RealAcct(db.Model):
    __tablename__ = 'real_acct'

    index = db.Column(db.BigInteger, primary_key=True)
    acct = db.Column(db.BigInteger)
    yr = db.Column(db.BigInteger)
    mailto = db.Column(db.Text)
    mail_addr_1 = db.Column(db.Text)
    mail_addr_2 = db.Column(db.Text)
    mail_city = db.Column(db.Text)
    mail_state = db.Column(db.Text)
    mail_zip = db.Column(db.Text)
    mail_country = db.Column(db.Text)
    undeliverable = db.Column(db.Text)
    str_pfx = db.Column(db.Text)
    str_num = db.Column(db.BigInteger)
    str_num_sfx = db.Column(db.Text)
    str = db.Column(db.Text)
    str_sfx = db.Column(db.Text)
    str_sfx_dir = db.Column(db.Text)
    str_unit = db.Column(db.Text)
    site_addr_1 = db.Column(db.Text)
    site_addr_2 = db.Column(db.Text)
    site_addr_3 = db.Column(db.Text)
    state_class = db.Column(db.Text)
    school_dist = db.Column(db.Text)
    map_facet = db.Column(db.Text)
    key_map = db.Column(db.Text)
    Neighborhood_Code = db.Column(db.Float)
    Neighborhood_Grp = db.Column(db.BigInteger)
    Market_Area_1 = db.Column(db.Text)
    Market_Area_1_Dscr = db.Column(db.Text)
    Market_Area_2 = db.Column(db.Text)
    Market_Area_2_Dscr = db.Column(db.Text)
    econ_area = db.Column(db.Text)
    econ_bld_class = db.Column(db.Text)
    center_code = db.Column(db.Text)
    yr_impr = db.Column(db.Text)
    yr_annexed = db.Column(db.Text)
    splt_dt = db.Column(db.Text)
    dsc_cd = db.Column(db.Text)
    nxt_bld = db.Column(db.BigInteger)
    bld_ar = db.Column(db.BigInteger)
    land_ar = db.Column(db.BigInteger)
    acreage = db.Column(db.Float)
    Cap_acct = db.Column(db.Text)
    shared_cad = db.Column(db.Text)
    land_val = db.Column(db.Float)
    bld_val = db.Column(db.Float)
    x_features_val = db.Column(db.Float)
    ag_val = db.Column(db.Float)
    assessed_val = db.Column(db.Float)
    tot_appr_val = db.Column(db.Float)
    tot_mkt_val = db.Column(db.Float)
    prior_land_val = db.Column(db.Float)
    prior_bld_val = db.Column(db.Float)
    prior_x_features_val = db.Column(db.Float)
