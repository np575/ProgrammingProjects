
CREATE TABLE IF NOT EXISTS `Appointments` (
                `id` int(11) NOT NULL AUTO_INCREMENT,
                `name` varchar(50) NOT NULL,
                `username` varchar(50) NOT NULL,
                `email` varchar(50) NOT NULL,
                `foodcontent` varchar(200) NOT NULL,
                `Pickupaddress` varchar(200) NOT NULL,
                `estimatednoofpeople` int(11) NOT NULL,
                `Phonenumber` int(10) NOT NULL,
                `trn_date` datetime NOT NULL,
                PRIMARY KEY (`id`)
                );

