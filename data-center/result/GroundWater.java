package com.yunli.ecology.multiplex.adaptersite.entity.wading.project;

/**
 * dwd_fzr_fss_wr_gws_b
 * 地下水水源地基本信息表
 */
@lombok.Data
public class GroundWater {

    /**
     * 地下水水源地代码
     */
    private String gwsCd;

    /**
     * 地下水水源地名称
     */
    private String gwsNm;

    /**
     * 地下水水源地面积
     */
    private Double gwsA;

    /**
     * 地下水水源地经度
     */
    private Double gwhsLong;

    /**
     * 地下水水源地纬度
     */
    private Double gwhsLat;

    /**
     * 地下水水源地所在位置
     */
    private String gwhsLoc;

    /**
     * 所取用地下水类型
     */
    private String grwaType;

    /**
     * 投入运行年
     */
    private String runYear;

    /**
     * 水质目标
     */
    private String waquGoal;

    /**
     * 水源类型
     */
    private String wasoType;

    /**
     * 主要取水用途
     */
    private String wainUse;

    /**
     * 规模以上机电井数量
     */
    private Integer wellNums;

    /**
     * 范围描述
     */
    private String rangDesc;

    /**
     * 建设状况
     */
    private String consCond;

    /**
     * 投产时间
     */
    private java.util.Date putProdTm;

    /**
     * 运行状况
     */
    private String runCond;

    /**
     * 多年平均年可开采量
     */
    private Double avgExpYd;

    /**
     * 供水对象
     */
    private String wsObj;

    /**
     * 供水对象类型
     */
    private String wsObjTp;

    /**
     * 主要供水城镇名称
     */
    private String wasuTownName;

    /**
     * 设计年取水量
     */
    private Double desInt;

    /**
     * 年许可取水量
     */
    private Double permInt;

    /**
     * 水源地管理单位代码
     */
    private String whsManCd;

    /**
     * 水源地审批单位代码
     */
    private String whsApprCd;

    /**
     * 监控级别
     */
    private String monG;

    /**
     * 是否为应急水源地
     */
    private String isEmg;

    /**
     * 时间戳
     */
    private java.util.Date ts;

    /**
     * 记录失效时间
     */
    private java.util.Date exprDate;

    /**
     * 备注
     */
    private String nt;

    /**
     * 来源部门
     */
    private String srcDep;

    /**
     * 来源系统
     */
    private String srcSys;

    /**
     * 数据插入时间
     */
    private String eventTime;

    /**
     * 日分区字段
     */
    private String pdate;
}
