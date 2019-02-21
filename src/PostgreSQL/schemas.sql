CREATE TABLE anime(
                     a_aid        integer,
                     a_atitle     varchar(255) NOT NULL,
                     a_aurl       varchar(255) NOT NULL,
                     a_aimg      varchar(2083),
                     a_adate     date,
                     PRIMARY KEY(a_id)
                     );

CREATE TABLE episode(
                     a_aid       integer,
                     e_epid      integer,
                     e_eptitle   varchar(255) NOT NULL,
                     e_eptitle2   varchar(255) ,
                     e_epurl     varchar(2083),
                     e_epdate    date,
                     PRIMARY KEY (e_epid),
                     FOREIGN KEY (a_aid) REFERENCES anime(a_aid)
                    );

CREATE TABLE userinfo(
                     u_username      varchar(20),
                     u_useremail     varchar(128),
                     PRIMARY KEY(u_username)
                     );

CREATE TABLE following(
                     f_username      varchar(20),
                     f_aid        integer,
                     FOREIGN KEY (f_username) REFERENCES userinfo(u_username),
                     FOREIGN KEY (f_aid) REFERENCES anime(a_aid)
                     UNIQUE (f_username, f_aid)
                     );