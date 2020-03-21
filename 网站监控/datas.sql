# Host: localhost  (Version: 5.0.96-community)
# Date: 2020-03-21 13:39:36
# Generator: MySQL-Front 5.3  (Build 4.234)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "datas"
#

DROP TABLE IF EXISTS `datas`;
CREATE TABLE `datas` (
  `Id` int(11) NOT NULL auto_increment,
  `time` varchar(255) default NULL,
  `code` varchar(255) default NULL,
  `url` varchar(255) default NULL,
  PRIMARY KEY  (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
