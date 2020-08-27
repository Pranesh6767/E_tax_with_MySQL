use freedb_etax2020;

CREATE TABLE `deleteddata` (
  `village` varchar(20) DEFAULT NULL,
  `uidnumber` varchar(20) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL
);

CREATE TABLE `deleteddataper` (
  `village` varchar(20) DEFAULT NULL,
  `uidnumber` varchar(20) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL
);

CREATE TABLE `kalamwadi` (
  `idnumber` varchar(10) DEFAULT NULL,
  `meternumber` varchar(10) DEFAULT NULL,
  `wardnumber` varchar(10) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `housetax` varchar(10) DEFAULT NULL,
  `healthtax` varchar(10) DEFAULT NULL,
  `lighttax` varchar(10) DEFAULT NULL,
  `watertax` varchar(10) DEFAULT NULL,
  `total` varchar(10) DEFAULT NULL,
  `reciptnumber` varchar(10) DEFAULT NULL,
  `housetaxpaid` varchar(10) DEFAULT NULL,
  `healthtaxpaid` varchar(10) DEFAULT NULL,
  `lighttaxpaid` varchar(10) DEFAULT NULL,
  `watertaxpaid` varchar(10) DEFAULT NULL,
  `totalpaid` varchar(10) DEFAULT NULL,
  `rest` varchar(10) DEFAULT NULL,
  `datei` varchar(50) DEFAULT NULL
);

CREATE TABLE `kalamwadiinfo` (
  `idnumber` varchar(10) DEFAULT NULL,
  `meternumber` varchar(10) DEFAULT NULL,
  `wardnumber` varchar(10) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `housetax` varchar(10) DEFAULT NULL,
  `healthtax` varchar(10) DEFAULT NULL,
  `lighttax` varchar(10) DEFAULT NULL,
  `watertax` varchar(10) DEFAULT NULL,
  `total` varchar(10) DEFAULT NULL,
  `rest` varchar(10) DEFAULT NULL
);

CREATE TABLE `kalamwadirec` (
  `rec` int(11) DEFAULT NULL
);

CREATE TABLE `kalmwadirec` (
  `rec` int(11) DEFAULT NULL
);

CREATE TABLE `passwords` (
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL
);

CREATE TABLE `updateddata` (
  `village` varchar(20) DEFAULT NULL,
  `idnumber` varchar(10) DEFAULT NULL,
  `meternumber` varchar(10) DEFAULT NULL,
  `wardnumber` varchar(10) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `housetax` varchar(10) DEFAULT NULL,
  `healthtax` varchar(10) DEFAULT NULL,
  `lighttax` varchar(10) DEFAULT NULL,
  `watertax` varchar(10) DEFAULT NULL,
  `total` varchar(10) DEFAULT NULL,
  `reciptnumber` varchar(10) DEFAULT NULL,
  `housetaxpaid` varchar(10) DEFAULT NULL,
  `healthtaxpaid` varchar(10) DEFAULT NULL,
  `lighttaxpaid` varchar(10) DEFAULT NULL,
  `watertaxpaid` varchar(10) DEFAULT NULL,
  `totalpaid` varchar(10) DEFAULT NULL,
  `rest` varchar(10) DEFAULT NULL
);

CREATE TABLE `updateddataper` (
  `village` varchar(20) DEFAULT NULL,
  `idnumber` varchar(10) DEFAULT NULL,
  `meternumber` varchar(10) DEFAULT NULL,
  `wardnumber` varchar(10) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `housetax` varchar(10) DEFAULT NULL,
  `healthtax` varchar(10) DEFAULT NULL,
  `lighttax` varchar(10) DEFAULT NULL,
  `watertax` varchar(10) DEFAULT NULL,
  `total` varchar(10) DEFAULT NULL,
  `reciptnumber` varchar(10) DEFAULT NULL,
  `housetaxpaid` varchar(10) DEFAULT NULL,
  `healthtaxpaid` varchar(10) DEFAULT NULL,
  `lighttaxpaid` varchar(10) DEFAULT NULL,
  `watertaxpaid` varchar(10) DEFAULT NULL,
  `totalpaid` varchar(10) DEFAULT NULL,
  `rest` varchar(10) DEFAULT NULL
);
