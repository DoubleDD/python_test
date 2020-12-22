package com.yunli.ecology.multiplex.adaptersite.entity.wading.project;

/**
 * adm_zhslyzt_qsk
 * 一张图取水口
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
     * 省级行政区划编码
     */
    private String provRegionCode;

    /**
     * 省级行政区划名称
     */
    private String provRegionName;

    /**
     * 市级行政区划编码
     */
    private String cityRegionCode;

    /**
     * 市级行政区划名称
     */
    private String cityRegionName;

    /**
     * 区县行政区划编码
     */
    private String regionCode;

    /**
     * 区县行政区划名称
     */
    private String regionName;

    /**
     * 水源类型
     */
    private String wainWasoType;

    /**
     * 水源地名称
     */
    private String wainWasoName;

    /**
     * 取水流量
     */
    private Integer wainFlow;

    /**
     * 规模类型
     */
    private String scalType;

    /**
     * 取水方式
     */
    private String intTp;

    /**
     * 开始取水日期
     */
    private java.util.Date fromIntDt;

    /**
     * 设计流量
     */
    private Double desQ;

    /**
     * 运行状况（工程特性）
     */
    private String runCond;

    /**
     * 主要取水用途（工程特性）
     */
    private String wainUse;

    /**
     * 许可总取水量（工程特性）
     */
    private Double permWw;

    /**
     * 取水量重复系数（工程特性）
     */
    private Double coefficient;

    /**
     * 取水许可证代码（管理情况）
     */
    private String watLicCode;

    /**
     * 管理单位代码（管理情况）
     */
    private String engManCd;

    /**
     * 管理单位名称（管理情况）
     */
    private String engManName;

    /**
     * 取水许可证审批单位（管理情况）
     */
    private String approvalUnit;

    /**
     * 水许可监督管理机关单位（管理情况）
     */
    private String managementAgency;

    /**
     * 关联的河流长度（关联情况）
     */
    private Double riverLakeLength;

    /**
     * 流域面积（关联情况）
     */
    private Double drainageArea;

    /**
     * 多年平均降水量（关联情况）
     */
    private Double averagePrecipitation;

    /**
     * 多年平均年径流深（关联情况）
     */
    private Double averageAnnualRunoffDepth;

    /**
     * 河流平均比降（关联情况）
     */
    private Double averageRiverDrop;

    /**
     * 河流code
     */
    private String rvCode;

    /**
     * 河流名称
     */
    private String rvName;
}
