from src.Dao.Daobase import Daobase
from datetime import datetime as dt
from datetime import timedelta


class NewHouseSourceDao(Daobase):
    '''向数据库中写入新房源信息'''
    @classmethod
    def __newhouse_source_project_sqlmaker(cls, project):
        columns = ['thedate', 'region', 'project_name', 'builder', 'address', 'house_useage', 'land_usage',
                   'land_years_limit', 'land_serial_num', 'land_contact_num', 'presale_license_num', 'pre_sale_count',
                   'pre_area', 'now_sale_count', 'now_area']
        sql = "insert into newhousesrc_project ({}) values('{}','{}','{}','{}','{}','{}','{}',{},'{}','{}','{}',{},{},{},{})".format(
            ','.join(columns),
            project['thedate'],
            project['region'],
            project['project_name'],
            project['builder'],
            project['address'],
            project['house_useage'],
            project['land_usage'],
            project['land_years_limit'],
            project['land_serial_num'],
            project['land_contact_num'],
            project['presale_license_num'],
            project['pre_sale_count'],
            project['pre_area'],
            project['now_sale_count'],
            project['now_area'])
        return sql

    @classmethod
    def __newhouse_source_project_infogetter(cls, project):
        return '{}'.format(project['project_name'])

    @classmethod
    def write_newhouse_project(cls, project):
        '''
        id serial NOT NULL, --id
        thedate date NOT NULL, --预售日期
        region character varying(255), --区域
        project_name character varying(255) NOT NULL, --项目名称
        builder character varying(255) NOT NULL, --开发商
        address character varying(255) NOT NULL, --地址
        house_useage character varying(255) NOT NULL, --房屋用途
        land_usage varchar(255),  --土地用途
        land_years_limit integer, --使用年限
        land_serial_num varchar(255), --土地宗地号
        land_contact_num varchar(255), --土地合同文号
        presale_license_num character varying(255) NOT NULL, --预售许可证
        pre_sale_count integer NOT NULL, -- 预售套数
        pre_area float,  --预售面积
        now_sale_count integer NOT NULL, -- 现售套数
        now_area float, --现售面积
        :return:
        '''
        return cls.writeoneitem(project, cls.__newhouse_source_project_sqlmaker, cls.__newhouse_source_project_infogetter)

    @classmethod
    def get_project_id(cls, project):
        sql = "select id from newhousesrc_project where presale_license_num = '{}'".format(project['presale_license_num'])
        rows = cls.select(sql)
        if len(rows) == 0:
            return 0
        return rows[0][0]

    @classmethod
    def __newhouse_source_building_sqlmaker(cls, building):
        '''
        id serial not null,
        project_id integer NOT NULL,
        project_name character varying(255) NOT NULL,
        building_name character varying(255) NOT NULL,
        plan_license character varying(255) NOT NULL,
        build_license character varying(255) NOT NULL,
        :param building:
        :return:
        '''
        columns = ['project_id', 'project_name', 'building_name', 'plan_license', 'build_license']
        sql = "insert into newhousesrc_building ({}) values({},'{}','{}','{}','{}')".format(
            ','.join(columns),
            building['project_id'],
            building['project_name'],
            building['building_name'],
            building['plan_license'],
            building['build_license'])
        return sql

    @classmethod
    def __newhouse_source_building_infogetter(cls, project):
        return '{}'.format(project['project_name'])

    @classmethod
    def write_newhouse_building(cls, building):
        '''
          id serial not null,
          project_id integer NOT NULL,
          project_name character varying(255) NOT NULL,
          building_name character varying(255) NOT NULL,
          plan_license character varying(255) NOT NULL,
          build_license character varying(255) NOT NULL,
        :param building:
        :return:
        '''
        return cls.writeoneitem(building, cls.__newhouse_source_building_sqlmaker, cls.__newhouse_source_building_infogetter)

    @classmethod
    def get_building_id(cls, building):
        sql = "select id from newhousesrc_building where project_id = {} and building_name='{}'".format(building['project_id'], building['building_name'])
        rows = cls.select(sql)
        if len(rows) == 0:
            return 0
        return rows[0][0]

    @classmethod
    def __newhosue_source_houselist_sqlmaker(cls, house):
        '''
        id serial not null,
        building_id int not null,
        building_name character varying(255), --几栋
        branch character varying(10),   --座号
        room_num character varying(50),
        floor integer,
        house_type character varying(255),
        contact_code character varying(255),
        price double precision,
        usage character varying(50),
        build_area double precision,
        inside_area double precision,
        share_area double precision,
        :param house:
        :return:
        '''
        columns = ['building_id', 'building_name', 'branch', 'room_num', 'floor', 'house_type', 'contact_code',
                   'price', 'usage', 'build_area', 'inside_area', 'share_area']
        sql = "insert into newhousesrc_house ({}) values({},'{}','{}','{}','{}','{}','{}','{}','{}',{},{},{})".format(
            ','.join(columns),
            house['building_id'],
            house['building_name'],
            house['branch'],
            house['room_num'],
            house['floor'],
            house['house_type'],
            house['contact_code'],
            house['price'],
            house['usage'],
            house['build_area'],
            house['inside_area'],
            house['share_area'],)
        return sql

    @classmethod
    def __write_newhouse_source_houselist_infogetter(cls, house):
        return '{}, {}'.format(house['branch'], house['room_num'])

    @classmethod
    def write_newhouse_source_houselist(cls, houselist):
        cls.writelist(houselist, cls.__newhosue_source_houselist_sqlmaker, cls.__write_newhouse_source_houselist_infogetter)