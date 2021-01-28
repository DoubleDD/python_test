package com.yunli.ecology.multiplex.adaptersite.entity.wading.project;

/**
 * adm_zhslyzt_dxs
 * 一张图地下水
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
     * 所取用地下水类型
     */
    private String grwaType;

    /**
     * 经度
     */
    private Double gwhsLong;

    /**
     * 纬度
     */
    private Double gwhsLat;

    /**
     * 地下水水源地所在位置
     */
    private String gwhsLoc;

    /**
     * 省级行政区划编码
     */
    private String provregioncode;

    /**
     * 省级行政区划名称
     */
    private String provregionname;

    /**
     * 市级行政区划编码
     */
    private String cityregioncode;

    /**
     * 市级行政区划名称
     */
    private String cityregionname;

    /**
     * 区县行政区划编码
     */
    private String regioncode;

    /**
     * 区县行政区划名称
     */
    private String regionname;

    /**
     * 所属地貌类型
     */
    private String dmType;

    /**
     * 水质类别
     */
    private String waquGoal;

    /**
     * 水源类型
     */
    private String wasoType;

    /**
     * 机电井数量
     */
    private Integer jdjNumber;

    /**
     * 取水口数量
     */
    private Integer qskNumber;

    /**
     * 设计年取水量
     */
    private Double desInt;

    /**
     * 年许可取水量（开发利用情况）
     */
    private Double permInt;

    /**
     * 投入运行年（开发利用情况）
     */
    private Double runYear;

    /**
     * 运行状况（开发利用情况）
     */
    private String runCond;

    /**
     * 主要取水用途（开发利用情况）
     */
    private String wainUse;

    /**
     * 管理单位代码（管理情况）
     */
    private String whsManCd;

    /**
     * 管理单位名称（管理情况）
     */
    private String whsManNm;

    /**
     * 所属河湖code
     */
    private String riverLakeCode;

    /**
     * 所属河湖名称
     */
    private String riverLakeName;
}
