package com.yunli.ecology.multiplex.adaptersite.entity.wading.project;

/**
 * dwd_fzr_fss_wr_sws_b
 * 地表水水源地基本信息表
 */
@lombok.Data
public class SurfaceWater {

    /**
     * 地表水水源地代码
     */
    private String swsCd;

    /**
     * 地表水水源地名称
     */
    private String swsNm;

    /**
     * 地表水水源地类型
     */
    private String swsTp;

    /**
     * 地表水水源地经度
     */
    private Double swhsLong;

    /**
     * 地表水水源地纬度
     */
    private Double swhsLat;

    /**
     * 地表水水源地所在位置
     */
    private String swhsLoc;

    /**
     * 取水水源类型
     */
    private String wainWasoType;

    /**
     * 水面面积
     */
    private Double watA;

    /**
     * 取水口数量
     */
    private Integer wainNum;

    /**
     * 主要取水用途
     */
    private String wainUse;

    /**
     * 水质目标
     */
    private String wqGoal;

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
     * 水源供水持续状况
     */
    private String wsCond;

    /**
     * 供水对象
     */
    private String wsObj;

    /**
     * 供水对象类型
     */
    private String wsObjTp;

    /**
     * 设计年供水人口
     */
    private Double dywsPp;

    /**
     * 设计年供水量
     */
    private Double dywsW;

    /**
     * 设计日供水量
     */
    private Double ddwsW;

    /**
     * 主要供水城镇名称
     */
    private String wasuTownName;

    /**
     * 投入运行年
     */
    private String runYear;

    /**
     * 水源地管理单位代码
     */
    private String whsManCd;

    /**
     * 水源地审批单位代码
     */
    private String whsApprCd;

    /**
     * 应急管理单位代码
     */
    private String emCd;

    /**
     * 监控级别
     */
    private String monG;

    /**
     * 一级保护区面积
     */
    private Double firProA;

    /**
     * 一级保护区水域面积（平方公里）
     */
    private Double prooLandArea;

    /**
     * 一级保护区陆域面积（平方公里）
     */
    private Double prooWaterArea;

    /**
     * 二级保护区面积
     */
    private Double secProA;

    /**
     * 二级保护区水域面积（平方公里）
     */
    private Double protLandA;

    /**
     * 二级保护区陆域面积（平方公里）
     */
    private Double protWaterArea;

    /**
     * 准保护区面积
     */
    private Double norProA;

    /**
     * 是否为应急水源地
     */
    private String isEmg;

    /**
     * 时间戳
     */
    private java.util.Date ts;

    /**
     * 备注
     */
    private String nt;

    /**
     * 记录失效时间
     */
    private java.util.Date exprDate;

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
