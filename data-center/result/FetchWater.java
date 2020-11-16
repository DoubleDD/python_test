package com.yunli.ecology.multiplex.adaptersite.entity.wading.project;

/**
 * dwd_fzr_fss_wr_int_b
 * 地表水取水口基本信息表
 */
@lombok.Data
public class FetchWater {

    /**
     * 地表水取水口代码
     */
    private String intCd;

    /**
     * 地表水取水口名称
     */
    private String intNm;

    /**
     * 取水口经度
     */
    private Double wainLong;

    /**
     * 取水口纬度
     */
    private Double wainLat;

    /**
     * 取水口所在位置
     */
    private String wainLoc;

    /**
     * 取水水源类型
     */
    private String wainWasoType;

    /**
     * 取水流量
     */
    private Integer wainFlow;

    /**
     * 规模类型
     */
    private String scalType;

    /**
     * 取水许可证代码
     */
    private String watLicCode;

    /**
     * 主要取水用途
     */
    private String wainUse;

    /**
     * 取水方式
     */
    private String intTp;

    /**
     * 开始取水日期
     */
    private java.util.Date fromIntDt;

    /**
     * 许可最大流量
     */
    private Double maxPermQ;

    /**
     * 设计流量
     */
    private Double desQ;

    /**
     * 许可总取水量
     */
    private Double permWw;

    /**
     * 运行状况
     */
    private String runCond;

    /**
     * 管理单位代码
     */
    private String engManCd;

    /**
     * 供水范围
     */
    private String wsReg;

    /**
     * 水量计算方法
     */
    private String intCalWay;

    /**
     * 是否为灌区渠首
     */
    private String isIrrhd;

    /**
     * 口门控制面积
     */
    private Double conIrrA;

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
