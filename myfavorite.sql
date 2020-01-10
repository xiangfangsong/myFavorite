/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80018
 Source Host           : localhost:3306
 Source Schema         : myfavorite

 Target Server Type    : MySQL
 Target Server Version : 80018
 File Encoding         : 65001

 Date: 07/01/2020 22:56:53
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for favorite
-- ----------------------------
DROP TABLE IF EXISTS `favorite`;
CREATE TABLE `favorite`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `wurl` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `uid` int(11) NOT NULL,
  `type` tinyint(255) NULL DEFAULT 1,
  `count` int(11) NULL DEFAULT 0,
  `ctime` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of favorite
-- ----------------------------
INSERT INTO `favorite` VALUES (2, 'baidu', 'http://www.baidu.com', 2, 0, 2, '2020-01-07 13:17:44');
INSERT INTO `favorite` VALUES (3, 'google', 'http://www.google.com', 1, 0, 10, '2020-01-07 18:35:28');
INSERT INTO `favorite` VALUES (4, '浙江工商大学', 'http://www.zjgsu.edu.cn', 2, 1, 0, '2020-01-07 19:38:51');
INSERT INTO `favorite` VALUES (5, 'youtube', 'http://www.youtube.com', 2, 0, 3, '2020-01-07 19:40:02');
INSERT INTO `favorite` VALUES (6, '浙江工商大学', 'http://www.zjgsu.edu.cn', 1, 1, 2, '2020-01-07 20:02:34');

-- ----------------------------
-- Table structure for login
-- ----------------------------
DROP TABLE IF EXISTS `login`;
CREATE TABLE `login`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `role` tinyint(255) NULL DEFAULT 0,
  `ctime` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of login
-- ----------------------------
INSERT INTO `login` VALUES (1, 'admin', '202cb962ac59075b964b07152d234b70', 1, '2020-01-07 11:22:09');
INSERT INTO `login` VALUES (2, 'user', 'e10adc3949ba59abbe56e057f20f883e', 0, '2020-01-07 12:54:54');

SET FOREIGN_KEY_CHECKS = 1;
