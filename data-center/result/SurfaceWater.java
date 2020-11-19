package com.yunli.ecology.multiplex.adaptersite.entity.wading.project;

/**
 * adm_zhslyzt_dbs
 * 一张图地表水
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
     * 经度
     */
    private Double swhsLong;

    /**
     * 纬度
     */
    private Double swhsLat;

    /**
     * 地表水水源地所在位置
     */
    private String swhsLoc;

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
     * 取水水源类型
     */
    private String wainWasoType;

    /**
     * 取水口数量
     */
    private String qskNumber;

    /**
     * 一级保护区水域面积
     */
    private Double prooLandArea;

    /**
     * 一级保护区陆域面积
     */
    private Double prooWaterArea;

    /**
     * 主要供水城镇名称（工程特性）
     */
    private String wasuTownName;

    /**
     * 主要取水用途（工程特性）
     */
    private String wainUse;

    /**
     * 取水许可证代码（管理情况）
     */
    private String watLicCode;

    /**
     * 管理单位代码（管理情况）
     */
    private String whsManCd;

    /**
     * 管理单位名称（管理情况）
     */
    private String whsManName;

    /**
     * 关联的河流code（关联情况）
     */
    private String riverLakeCode;

    /**
     * 关联的河流名称（关联情况）
     */
    private String riverLakeName;

    /**
     * 关联的河流长度（关联情况）
     */
    private Double riverLakeLength;

    /**
     * 流域面积（关联情况）
     */
    private Double drainagearea;

    /**
     * 多年平均降水量（关联情况）
     */
    private Double averageprecipitation;

    /**
     * 多年平均年径流深（关联情况）
     */
    private Double averageannualrunoffdepth;

    /**
     * 河流平均比降（关联情况）
     */
    private Double averageriverdrop;
}
