-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: bilibili
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `collection`
--

DROP TABLE IF EXISTS `collection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collection` (
  `mname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cname` varchar(255) NOT NULL,
  `cintro` text,
  `cvideo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cname`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collection`
--

LOCK TABLES `collection` WRITE;
/*!40000 ALTER TABLE `collection` DISABLE KEYS */;
INSERT INTO `collection` VALUES ('天津博物馆','万历漳州窑红绿彩罗经文盘','高8厘米 口径39厘米 足径18厘米','https://baike.baidu.com/isdf'),('洛阳博物馆','兽面纹铜方鼎','这件兽面纹鼎不仅体形较大而且纹饰极为精美，是西周青铜鼎的杰出代表。','https://baike.baidu.com/itsd/ds'),('北京博物馆','玉器','由一块大的翡翠料抛开制成一对，高42.8厘米，口径9.6×5.4厘米。淡翠绿色，间少许淡粉色，色泽均匀柔和，美丽晶莹。盖有桃形钮，盖身及瓶两侧镂雕缠枝菊花纹','https://www.msn.cn/zh-cn/news/nationa'),('湖北省博物馆','越王勾践剑',' 时期为春秋晚期，千年不锈，由许多小暗格组成。1965年江陵望山1号墓出土，长55.7厘米。','https://www.msn.cn/zh-cn/news/nationa');
/*!40000 ALTER TABLE `collection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cvideo`
--

DROP TABLE IF EXISTS `cvideo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cvideo` (
  `mname` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `cvname` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `cvurl` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `cvtime` datetime DEFAULT NULL,
  `cvstatus` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `cvid` bigint(20) NOT NULL,
  PRIMARY KEY (`cvid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cvideo`
--

LOCK TABLES `cvideo` WRITE;
/*!40000 ALTER TABLE `cvideo` DISABLE KEYS */;
INSERT INTO `cvideo` VALUES ('北京博物馆','青铜器','https://baike.baidu.com/item','2021-05-18 23:48:39','审核通过',12),('洛阳博物馆','母鼓铜方罍','https://baike.baidu.com/itsd/ds','2021-05-16 21:34:41','待审核',122),('湖北省博物馆','曾侯乙编钟','https://baike.baidu.com/weu','2021-05-13 23:47:53','审核不通过',123),('天津博物馆','尚均雕寿山石弥勒像','https://baike.baidu.com/isdf','2021-05-01 21:35:07','待审核',2141);
/*!40000 ALTER TABLE `cvideo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evideo`
--

DROP TABLE IF EXISTS `evideo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `evideo` (
  `evid` bigint(20) NOT NULL,
  `evname` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `mname` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `evtime` datetime DEFAULT NULL,
  `evurl` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `evstatus` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`evid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evideo`
--

LOCK TABLES `evideo` WRITE;
/*!40000 ALTER TABLE `evideo` DISABLE KEYS */;
INSERT INTO `evideo` VALUES (12342,'天津博物馆展览','天津博物馆','2021-05-12 21:20:42','https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1','待审核'),(121241,'洛阳博物馆展览','洛阳博物馆','2021-05-28 21:17:50','http://baidu.com/lymuseum','待审核'),(214124,'新展览视频','湖北省博物馆','2021-04-27 21:18:18','http://baidu.com/hbmuseum','审核不通过'),(837837,'展览视频新版本','北京博物馆','2021-05-04 21:01:41','https://www.baidu.com/332','审核通过');
/*!40000 ALTER TABLE `evideo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `examine`
--

DROP TABLE IF EXISTS `examine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `examine` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `examine`
--

LOCK TABLES `examine` WRITE;
/*!40000 ALTER TABLE `examine` DISABLE KEYS */;
INSERT INTO `examine` VALUES (1,'审核通过'),(2,'审核不通过');
/*!40000 ALTER TABLE `examine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exhibition`
--

DROP TABLE IF EXISTS `exhibition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exhibition` (
  `mname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `exname` varchar(255) DEFAULT NULL,
  `extime` date DEFAULT NULL,
  `exaddr` varchar(255) DEFAULT NULL,
  `exintro` text,
  `exvedio` varchar(255) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exhibition`
--

LOCK TABLES `exhibition` WRITE;
/*!40000 ALTER TABLE `exhibition` DISABLE KEYS */;
INSERT INTO `exhibition` VALUES ('洛阳博物馆','展览视频','2021-05-12','洛阳北华路20号','有各类文物、标本20万余件（套），其中一级文物近千件（套）。藏品绝大多数来自考古发掘和各地征集，其中以出土文物为主，既有浓郁、鲜明的地方色彩，又具有时代特征，基本反映着湖北地区古代文化的面貌。','http://baidu.com/lymuseum',9),('北京博物馆','新展览视频','2021-05-20','北京南涧路28号','原始人类的故事','http://baidu.com/museumstudy',11),('湖北省博物馆','回归生活','2021-05-13','湖北省武汉大学','生活的美好','http://baidu.com/goodlive',12),('天津博物馆','拥抱自然','2021-05-06','天津运动场','人与自然','https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1',13);
/*!40000 ALTER TABLE `exhibition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log` (
  `uname` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `time` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `src` varchar(1024) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=304 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` VALUES ('吼吼','/login','1621756007357',286,'登录'),('吼吼','/login','1621756063031',287,'登录'),('吼吼','/addstaff','1621756119286',288,'{用户名称:123};{用户密码:3s574423};{用户联系方式:13240958566};{用户id:1}'),('吼吼','/update','1621756145558',289,'{原用户名:123};{原用户密码:3s574423};{原用户联系方式:13240958566};{原用户id:1};{新用户名:123456};{新用户密码:3s574423};{新用户联系方式:13240958563};{新用户id:3}'),('吼吼','/removestaff','1621756159571',290,'{用户名称:123456};{用户密码:3s574423};{用户联系方式:13240958563};{用户id:3}'),('吼吼','/agreemvideo','1621756173877',291,'{博物馆名称:湖北省博物馆};{原视频url:http://phpvideo.com/4245};{新视频url:http://phpvideo.com/4245};{新视频审核状态:审核通过}'),('吼吼','/disagreemvideo','1621756177540',292,'{新视频标题:宣传视频};{新视频url:http://phpvideo.com/4245};{新视频审核状态:审核不通过}'),('吼吼','/disagreemvideo','1621756183073',293,'{新视频标题:宣传视频};{新视频url:http://studyvideo.com/13};{新视频审核状态:审核不通过}'),('吼吼','/agreemvideo','1621756185590',294,'{博物馆名称:洛阳博物馆};{原视频url:http://baike.com/329};{新视频url:http://baike.com/329};{新视频审核状态:审核通过}'),('吼吼','/removemvideo','1621756191746',295,'{博物馆名字:湖北省博物馆};{视频标题:湖北省博物馆};{上传时间:Sun May 23 2021 15:35:46 GMT+0800 (中国标准时间)};{视频url:湖北省博物馆http://phpvideo.com/4245};{审核状态:待审核}'),('吼吼','/addmuseum','1621756251309',296,'{博物馆名称:你说的};{博物馆介绍:打撒阿斯顿};{开放时间:9.30-17.30};{博物馆地址:四大奥多所};{文教活动:的强大撒奥所多};{科教活动:打撒撒大所多};{博物馆视频:大阿斯蒂芬斯蒂芬}'),('吼吼','/updatemuseum','1621756280444',297,'{原博物馆名称:你说的};{原博物馆介绍:打撒阿斯顿};{原开放时间:9.30-17.30};{原博物馆地址:四大奥多所};{原文教活动:的强大撒奥所多};{原科教活动:打撒撒大所多};{原博物馆视频:大阿斯蒂芬斯蒂芬};{新博物馆名称:你说的};{新博物馆介绍:打撒阿};{新开放时间:9.30-17.30};{新博物馆地址:四大};{新文教活动:的强大撒};{新科教活动:打撒撒大252};{新博物馆视频:大阿斯蒂芬斯蒂芬25}'),('吼吼','/removemuseum','1621756289895',298,'{博物馆名称:你说的};{博物馆介绍:你说的};{开放时间:9.30-17.30};{博物馆地址:四大};{文教活动:的强大撒};{科教活动:打撒撒大252};{博物馆视频:大阿斯蒂芬斯蒂芬25}'),('吼吼','/updatescorestatus','1621756307518',299,'{原权限:不可评论};{新权限:可评论}'),('吼吼','/updatescorestatus','1621756308446',300,'{原权限:可评论};{新权限:不可评论}'),('吼吼','/updatescorestatus','1621756309247',301,'{原权限:可评论};{新权限:不可评论}'),('吼吼','/updatescorestatus','1621756312201',302,'{原权限:不可评论};{新权限:可评论}'),('吼吼','/updatescorestatus','1621756317967',303,'{原权限:可评论};{新权限:不可评论}');
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `museum`
--

DROP TABLE IF EXISTS `museum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `museum` (
  `mname` varchar(255) NOT NULL,
  `mintro` text,
  `mtime` varchar(255) DEFAULT NULL,
  `maddr` varchar(255) DEFAULT NULL,
  `mactivity` text,
  `mresearch` text,
  `mvedio` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`mname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `museum`
--

LOCK TABLES `museum` WRITE;
/*!40000 ALTER TABLE `museum` DISABLE KEYS */;
INSERT INTO `museum` VALUES ('北京博物馆','北京博物馆','9:30 - 17:00','北京市中心天安门广场东侧','是一座系统展示中华民族文化历史的综合性博物馆，也是世界上最大的博物馆之一','国博藏品数量为100余万件，集收藏、研究、展览于一身','blob:https://baike.baidu.com/41ece1d9-1348-4a8e-b095-e7085cbba3ad'),('洛阳博物馆','洛阳博物馆创建于1958年，位于河南省洛阳市洛龙区隋唐里坊区西北隅，北临洛浦公园，南接洛阳植物园，环境优美，交通便利，是洛阳市的文化地标。','9:30 - 17:00','河南省洛阳市洛龙区隋唐里坊区西北隅','洛阳博物馆始终坚持收藏保管、宣传教育和科学研究相结合，充分发挥藏品优势','《四部备要》、《四部丛刊》、《二十四史》等历史文籍和《考古》、《文物》等学术刊物2000多册','http://baike.com/329'),('湖北省博物馆','湖北省博物馆筹建于1953年，坐落于湖北省武汉市武昌区东湖风景区，占地面积81909平方米，建筑面积49611平方米，展厅面积13427平方米，有中国规模最大的古乐器陈列馆。','9:00 - 17:00','湖北省武汉市武昌区东湖风景区','藏品绝大多数来自考古发掘和各地征集，其中以出土文物为主，既有浓郁、鲜明的地方色彩，又具有时代特征','《云梦睡虎地秦墓》、《睡虎地秦简文字编》，《曾侯乙墓》、《曾侯乙编钟研究》、《曾侯乙墓文物艺术》等','http://phpvideo.com/4245');
/*!40000 ALTER TABLE `museum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mvideo`
--

DROP TABLE IF EXISTS `mvideo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mvideo` (
  `mvid` bigint(20) NOT NULL AUTO_INCREMENT,
  `mname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `mvname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `mvtime` datetime DEFAULT NULL,
  `mvurl` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `mvstatus` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`mvid`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=448 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mvideo`
--

LOCK TABLES `mvideo` WRITE;
/*!40000 ALTER TABLE `mvideo` DISABLE KEYS */;
INSERT INTO `mvideo` VALUES (12,'洛阳博物馆','介绍视频','2021-05-25 21:00:31','http://baike.com/329','审核通过'),(25,'北京博物馆','宣传视频','2021-04-29 20:09:53','http://studyvideo.com/13','审核不通过'),(34,'湖北省博物馆','宣传视频','2021-05-20 21:12:09','http://phpvideo.com/4245','审核不通过');
/*!40000 ALTER TABLE `mvideo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nnews`
--

DROP TABLE IF EXISTS `nnews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nnews` (
  `mname` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `nname` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `ntime` date DEFAULT NULL,
  `nintro` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `nsource` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `nurl` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `nstatus` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  PRIMARY KEY (`nname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nnews`
--

LOCK TABLES `nnews` WRITE;
/*!40000 ALTER TABLE `nnews` DISABLE KEYS */;
INSERT INTO `nnews` VALUES ('湖北省博物馆','拥抱科技，回忆过去','2021-05-19','湖北博物馆的四大宝：出土于“曾侯乙墓”的曾侯乙编钟；冷兵器时代的精品之作越王勾践剑；距今100万年的郧县人头骨化石；元青花瓷中的珍品：四爱图梅瓶。馆内的日常展览，还具有鲜明的古楚文化和古长江文明的特征。','今日头条','https://you.ctrip.com/sight/wuhan145/8977.html','no'),('天津博物馆','新闻1','2021-05-17','关于天津的第一印象是天津狗不理包子和天津大麻花，但是我想这一定不是代表天津最经典的所在，于是决定去天津博物馆看看，我想在这里应该能找到我想要的！','百度百科','https://baijiahao.baidu.com/s?id=1659019844585063002&wfr=spider&for=pc','yes');
/*!40000 ALTER TABLE `nnews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (1,'管理员'),(2,'后台用户'),(3,'手机用户');
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `score`
--

DROP TABLE IF EXISTS `score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `score` (
  `mname` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `uname` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `evalscore` int(255) DEFAULT NULL,
  `evalintro` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `evalscore_ex` int(255) DEFAULT NULL,
  `evalscore_serv` int(255) DEFAULT NULL,
  `evalscore_environ` int(255) DEFAULT NULL,
  `scorestatus` int(4) DEFAULT NULL,
  PRIMARY KEY (`uname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `score`
--

LOCK TABLES `score` WRITE;
/*!40000 ALTER TABLE `score` DISABLE KEYS */;
INSERT INTO `score` VALUES ('洛阳博物馆','bacek',3,'节假日人多排队时间长，要么一大早，如果错过了，那就下午去，这样避开人多时段入内最快。',3,4,3,0),('北京博物馆','lasr',4,'强烈推荐青铜馆，精品太多了，器型精美，做工精细，很多有铭文。还有其他几个专题展厅，如书法厅，有米芾、赵构等真迹。印章厅，各朝代印章的发展过程。',5,5,5,1),('湖北省博物馆','sunyang',1,'我是中午去的，没有排队，直接就进去了，可以带水，会让自己喝一口。参观后挺震撼的，感叹一下，中国文化，博大精深，要是全部都仔细看的话要花很长的时间，我花了大概3小时，',2,2,4,0);
/*!40000 ALTER TABLE `score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `section`
--

DROP TABLE IF EXISTS `section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `section` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `super` int(255) DEFAULT NULL,
  `path` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `section`
--

LOCK TABLES `section` WRITE;
/*!40000 ALTER TABLE `section` DISABLE KEYS */;
INSERT INTO `section` VALUES (1,'用户管理',0,'user'),(2,'讲解审核',0,'verify'),(3,'数据管理',0,'manage'),(4,'数据备份和恢复',0,'bcre'),(5,'用户列表',1,'list'),(6,'博物馆视频审核',2,'mvideo'),(7,'展览视频审核',2,'evideo'),(8,'藏品视频审核',2,'cvideo'),(9,'博物馆',3,'museum'),(10,'近期展览',3,'exhibition'),(11,'经典藏品',3,'collection'),(12,'新闻',3,'news'),(13,'评价',3,'score'),(14,'日志及数据库操作',4,'updown');
/*!40000 ALTER TABLE `section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `upwd` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `uphone` varchar(255) DEFAULT NULL,
  `poid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=200529081 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (200529052,'吼吼','123456qw','13240525888',1),(200529073,'12321','123423d','13248924289',3),(200529036,'effsd','fdsfds12','13240958566',2),(200529037,'123456','123456qw','13240958566',1),(200529054,'2323','123465q','13244555555',1),(200529058,'asdad','dsadas12','13240958566',2),(200529059,'ewqeqw','dasdas12','13240958566',1),(200529060,'yjfhf','hdfgdgd32','13240958566',1),(200529061,'dfs','fsdsdfs12','13240958566',3),(200529062,'ads','sdadsadsa12','13240958566',1),(200529063,'sdad','dsaasd21','13240958566',2),(200529064,'dczzcx','zcxzxcczx12','13240958566',2),(200529065,'sadad','adssad1','13240958566',2),(200529066,'edf','sdfdfs11','13240958566',3),(200529068,'asdsda','sdadsa12','13240958566',1),(200529069,'asdsda','asdsad1','13240958566',3),(200529070,'龙哥','dasdsa1','13240958566',1),(200529071,'大萨达','1231ds','13248485364',3);
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-23 15:52:58
