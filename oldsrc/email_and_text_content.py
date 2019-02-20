import psycopg2
import boto3
import email_templete
from botocore.exceptions import ClientError

def get_array(date):
    conn = psycopg2.connect("host=3.94.63.239 port=5432 dbname=anime user=anime password=anime")
    print('connect to PostgreSQL success')
    cur = conn.cursor()
    cur.execute('''
        create temporary view etoday as select * from episode where e_epdate = '{}' ;
        create temporary view etoday2 as select e_aid, e_epid, e_epfulltitle, e_epurl,f_username from etoday inner join following on e_aid = f_aid;
        create temporary view etoday3 as select * from etoday2 left join anime on a_aid = e_aid;
        create temporary view etoday5 as select f_username , array_agg(array[a_atitle,a_aimg, e_epfulltitle,e_epurl]) from etoday3 group by f_username ;
        select u_username, u_useremail, array_agg  from etoday5 left join userinfo on u_username = f_username order by f_username;
              ;'''.format(date))
    rows = cur.fetchall()
    print(rows[1])
    # conn.commit()
    cur.close()
    conn.close()
    return rows

def make_it_html(line):
    content11 = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html style="width:100%;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0;">
 <head>
  <meta charset="UTF-8">
  <meta content="width=device-width, initial-scale=1" name="viewport">
  <meta name="x-apple-disable-message-reformatting">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta content="telephone=no" name="format-detection">
  <title>Back to School</title>
  <!--[if (mso 16)]>
    <style type="text/css">
    a {text-decoration: none;}
    </style>
    <![endif]-->
  <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]-->

  <style type="text/css">
@media only screen and (max-width:600px) {p, ul li, ol li, a { font-size:16px!important; line-height:150%!important } h1 { font-size:30px!important; text-align:center; line-height:120%!important } h2 { font-size:22px!important; text-align:center; line-height:120%!important } h3 { font-size:20px!important; text-align:center; line-height:120%!important } h1 a { font-size:30px!important } h2 a { font-size:22px!important } h3 a { font-size:20px!important } .es-menu td a { font-size:18px!important } .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a { font-size:14px!important } .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a { font-size:14px!important } .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a { font-size:12px!important } *[class="gmail-fix"] { display:none!important } .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 { text-align:center!important } .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 { text-align:right!important } .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 { text-align:left!important } .es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img { display:inline!important } .es-button-border { display:inline-block!important } a.es-button { font-size:16px!important; display:inline-block!important } .es-btn-fw { border-width:10px 0px!important; text-align:center!important } .es-adaptive table, .es-btn-fw, .es-btn-fw-brdr, .es-left, .es-right { width:100%!important } .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header { width:100%!important; max-width:600px!important } .es-adapt-td { display:block!important; width:100%!important } .adapt-img { width:100%!important; height:auto!important } .es-m-p0 { padding:0px!important } .es-m-p0r { padding-right:0px!important } .es-m-p0l { padding-left:0px!important } .es-m-p0t { padding-top:0px!important } .es-m-p0b { padding-bottom:0!important } .es-m-p20b { padding-bottom:20px!important } .es-mobile-hidden, .es-hidden { display:none!important } .es-desk-hidden { display:table-row!important; width:auto!important; overflow:visible!important; float:none!important; max-height:inherit!important; line-height:inherit!important } .es-desk-menu-hidden { display:table-cell!important } table.es-table-not-adapt, .esd-block-html table { width:auto!important } table.es-social { display:inline-block!important } table.es-social td { display:inline-block!important } }
#outlook a {
    padding:0;
}
.ExternalClass {
    width:100%;
}
.ExternalClass,
.ExternalClass p,
.ExternalClass span,
.ExternalClass font,
.ExternalClass td,
.ExternalClass div {
    line-height:100%;
}
.es-button {
    mso-style-priority:100!important;
    text-decoration:none!important;
}
a[x-apple-data-detectors] {
    color:inherit!important;
    text-decoration:none!important;
    font-size:inherit!important;
    font-family:inherit!important;
    font-weight:inherit!important;
    line-height:inherit!important;
}
.es-desk-hidden {
    display:none;
    float:left;
    overflow:hidden;
    width:0;
    max-height:0;
    line-height:0;
    mso-hide:all;
}
</style>
 </head>
 <body style="width:100%;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0;">
  <div class="es-wrapper-color" style="background-color:#F6F6F6;">

   <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top;">
     <tr style="border-collapse:collapse;">
      <td valign="top" style="padding:0;Margin:0;">
       <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
         <tr style="border-collapse:collapse;">
          <td class="es-adaptive" align="center" style="padding:0;Margin:0;">
           <table class="es-content-body" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;" width="600" cellspacing="0" cellpadding="0" align="center">
             <tr style="border-collapse:collapse;">
              <td align="left" style="padding:10px;Margin:0;">
               <!--[if mso]><table width="580"><tr><td width="280" valign="top"><![endif]-->


               <table class="es-right" cellspacing="0" cellpadding="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right;">
                 <tr style="border-collapse:collapse;">
                  <td width="280" align="left" style="padding:0;Margin:0;">
                   <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                     <tr style="border-collapse:collapse;">

                     </tr>
                   </table> </td>
                 </tr>
               </table>
               <!--[if mso]></td></tr></table><![endif]--> </td>
             </tr>
           </table> </td>
         </tr>
       </table>
       <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
         <tr style="border-collapse:collapse;">
         </tr>
         <tr style="border-collapse:collapse;">
          <td align="center" style="padding:0;Margin:0;">
           <table class="es-header-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;">
             <tr style="border-collapse:collapse;">
              <td align="left" style="padding:0;Margin:0;">
               <!--[if mso]><table width="600" cellpadding="0"
                            cellspacing="0"><tr><td width="160" valign="top"><![endif]-->
               <table class="es-left" cellspacing="0" cellpadding="0" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                 <tr style="border-collapse:collapse;">
                  <td class="es-m-p0r" width="160" valign="top" align="center" style="padding:0;Margin:0;">
                   <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                     <tr style="border-collapse:collapse;">
                      <td class="es-m-txt-c" align="left" style="Margin:0;padding-top:20px;padding-bottom:10px;padding-left:20px;padding-right:20px;"> <h2 style="Margin:0;line-height:40px;mso-line-height-rule:exactly;font-family:'trebuchet ms', 'lucida grande', 'lucida sans unicode', 'lucida sans', tahoma, sans-serif;font-size:40px;font-style:normal;font-weight:bold;color:#f55e61;">AnimeToday</h2> </td>
                     </tr>
                   </table> </td>
                 </tr>
               </table>
               <!--[if mso]></td><td width="20"></td><td width="420" valign="top"><![endif]-->
               <table cellspacing="0" cellpadding="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                 <tr style="border-collapse:collapse;">
                  <td width="420" align="left" style="padding:0;Margin:0;">
                   <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                     <tr class="es-hidden" style="border-collapse:collapse;">
                      <td align="center" style="padding:0;Margin:0;padding-top:15px;padding-left:20px;padding-right:20px;">
                       <table width="100%" height="100%" cellspacing="0" cellpadding="0" border="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                         <tr style="border-collapse:collapse;">
                          <td style="padding:0;Margin:0px;border-bottom:1px solid #FFFFFF;background:rgba(0, 0, 0, 0) none repeat scroll 0% 0%;height:1px;width:100%;margin:0px;"></td>
                         </tr>
                       </table> </td>
                     </tr>

                   </table> </td>
                 </tr>
               </table>
               <!--[if mso]></td></tr></table><![endif]--> </td>
             </tr>
             <tr style="border-collapse:collapse;">
              <td align="left" style="padding:0;Margin:0;">
               <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                 <tr style="border-collapse:collapse;">
                  <td width="600" valign="top" align="center" style="padding:0;Margin:0;">
                   <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">

                   </table> </td>
                 </tr>
               </table> </td>
             </tr>
           </table> </td>
         </tr>
       </table>
       <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
         <tr style="border-collapse:collapse;">
         </tr>
         <tr style="border-collapse:collapse;">
          <td align="center" style="padding:0;Margin:0;">
           <table class="es-header-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;">
             <tr style="border-collapse:collapse;">
              <td align="left" style="padding:0;Margin:0;">
               <!--[if mso]><table width="600" cellpadding="0"
                            cellspacing="0"><tr><td width="160" valign="top"><![endif]-->
               <table class="es-left" cellspacing="0" cellpadding="0" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                 <tr style="border-collapse:collapse;">
                  <td class="es-m-p0r" width="460" valign="top" align="center" style="padding:0;Margin:0;">
                   <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                     <tr style="border-collapse:collapse;">
                      <td class="es-m-txt-c" align="left" style="Margin:0;padding-top:0px;padding-bottom:0px;padding-left:20px;padding-right:20px;"> <h2 style="Margin:0;line-height:10px;mso-line-height-rule:exactly;font-family:'trebuchet ms', 'lucida grande', 'lucida sans unicode', 'lucida sans', tahoma, sans-serif;font-size:10px;font-style:normal;font-weight:bold;color:# ;">Hi """
    content12 = """! Welcome to Anime World!</h2> </td>
                     </tr>
                   </table> </td>
                 </tr>
               </table>

               <!--[if mso]></td><td width="20"></td><td width="420" valign="top"><![endif]-->
               <table cellspacing="0" cellpadding="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                 <tr style="border-collapse:collapse;">
                  <td width="420" align="left" style="padding:0;Margin:0;">
                   <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                     <tr class="es-hidden" style="border-collapse:collapse;">
                      <td align="center" style="padding:0;Margin:0;padding-top:15px;padding-left:20px;padding-right:20px;">
                       <table width="100%" height="100%" cellspacing="0" cellpadding="0" border="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                         <tr style="border-collapse:collapse;">
                          <td style="padding:0;Margin:0px;border-bottom:1px solid #FFFFFF;background:rgba(0, 0, 0, 0) none repeat scroll 0% 0%;height:1px;width:100%;margin:0px;"></td>
                         </tr>
                       </table> </td>
                     </tr>

                   </table> </td>
                 </tr>
               </table>
               <!--[if mso]></td></tr></table><![endif]--> </td>
             </tr>
             <tr style="border-collapse:collapse;">
              <td align="left" style="padding:0;Margin:0;">
               <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                 <tr style="border-collapse:collapse;">
                  <td width="600" valign="top" align="center" style="padding:0;Margin:0;">
                   <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">

                   </table> </td>
                 </tr>
               </table> </td>
             </tr>
           </table> </td>
         </tr>
       </table>
       <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
         <tr style="border-collapse:collapse;">
          <td align="center" style="padding:0;Margin:0;">
           <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;">
             <tr style="border-collapse:collapse;">
              <td align="left" style="padding:0;Margin:0;">
               <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                 <tr style="border-collapse:collapse;">
                  <td width="600" valign="top" align="center" style="padding:0;Margin:0;">
                   <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                     <tr style="border-collapse:collapse;">
                      <td style="padding:0;Margin:0;position:relative;" align="center"> <a target="_blank" href="https://viewstripo.email/" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;font-size:16px;text-decoration:none;color:#F1C232;"> <img class="adapt-img" src="https://github.com/sainas/AnimeToday/blob/master/animetoday.png?raw=true" alt="Back to school sale 30% Off" title="Back to school sale 30% Off" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="100%"></a> </td>
                     </tr>
                   </table> </td>
                 </tr>
               </table> </td>
             </tr>
           </table> </td>
         </tr>
       </table>"""
    contentmiddle = line[0]
    content1=content11+contentmiddle+content12
    content3="""<table class="es-footer" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top;">
         <tr style="border-collapse:collapse;">
          <td align="center" style="padding:0;Margin:0;">
           <table class="es-footer-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#31cb4b" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;">
             <tr style="border-collapse:collapse;">
              <td align="left" style="padding:0;Margin:0;">
               <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                 <tr style="border-collapse:collapse;">
                  <td width="600" valign="top" align="center" style="padding:0;Margin:0;">
                   <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">




                   </table> </td>
                 </tr>
               </table> </td>
             </tr>

             <tr style="border-collapse:collapse;">
              <td align="left" style="padding:15px;Margin:0;">
               <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                 <tr style="border-collapse:collapse;">
                  <td width="570" valign="top" align="center" style="padding:0;Margin:0;">
                   <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                     <tr style="border-collapse:collapse;">
                      <td class="es-m-txt-c" esdev-links-color="#666666" align="left" style="padding:0;Margin:0;padding-bottom:5px;"> <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:12px;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;line-height:18px;color:#666666;">© AnimeToday</p> </td>
                     </tr>
                     <tr style="border-collapse:collapse;">
                      <td class="es-m-txt-c" esdev-links-color="#666666" align="left" style="padding:0;Margin:0;"> <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:12px;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;line-height:18px;color:#666666;">You are receiving this email because you have subscribed AnimeToday new episodes alert service. If you would not like to receive this email, I haven't figure out how to let you <strong><a target="_blank" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;font-size:12px;text-decoration:none;color:#666666;" href="https://github.com/sainas/AnimeToday">unsubscribe</a></strong>.</p> </td>
                     </tr>
                   </table> </td>
                 </tr>
               </table> </td>
             </tr>
           </table> </td>
         </tr>
       </table>

     </tr>
   </table>
  </div>
 </body>
</html>"""
    content2 = ""
    num= 0
    for i in range(len(line[2])):
        animename = line[2][num][0]
        animeurl = line[2][num][1]
        eptitle = line[2][num][2]
        epfulltitle = 'https://www.crunchyroll.com' + line[2][num][3]
        num = num + 1
        onecontent = """<table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;">
         <tr style="border-collapse:collapse;">
          <td align="center" style="padding:0;Margin:0;">
           <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;">
             <tr style="border-collapse:collapse;">
              <td style="padding:0;Margin:0;padding-top:10px;background-repeat:repeat;" align="left">
               <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                 <tr style="border-collapse:collapse;">
                  <td width="600" valign="top" align="center" style="padding:0;Margin:0;">
                   <table style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;border-bottom:2px solid #22A4DD;" width="100%" cellspacing="0" cellpadding="0">
                     <tr style="border-collapse:collapse;">
                      <td class="es-m-txt-c" align="left" style="Margin:0;padding-top:5px;padding-bottom:10px;padding-left:20px;padding-right:20px;"> <h2 style="Margin:0;line-height:26px;mso-line-height-rule:exactly;font-family:'trebuchet ms', 'lucida grande', 'lucida sans unicode', 'lucida sans', tahoma, sans-serif;font-size:22px;font-style:normal;font-weight:normal;color:#22A4DD;">{}</h2> </td>
                     </tr>
                   </table> </td>
                 </tr>
               </table> </td>
             </tr>
             <tr style="border-collapse:collapse;">
              <td align="left" style="Margin:0;padding-bottom:15px;padding-top:20px;padding-left:20px;padding-right:20px;">
               <!--[if mso]><table width="560" cellpadding="0"
                        cellspacing="0"><tr><td width="270" valign="top"><![endif]-->
               <table class="es-left" cellspacing="0" cellpadding="0" align="left" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:left;">
                 <tr style="border-collapse:collapse;">
                  <td width="270" align="left" style="padding:0;Margin:0;">
                   <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                     <tr style="border-collapse:collapse;">
                      <td align="center" style="padding:0;Margin:0;"> <a target="_blank" href="https://viewstripo.email/" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;font-size:16px;text-decoration:none;color:#F1C232;"> <img class="adapt-img" src="{}" alt="" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;" width="215"> </a> </td>
                     </tr>
                   </table> </td>
                 </tr>
               </table>
               <!--[if mso]></td><td width="20"></td><td width="270" valign="top"><![endif]-->
               <table class="es-right" cellspacing="0" cellpadding="0" align="right" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;float:right;">
                 <tr style="border-collapse:collapse;">
                  <td class="es-m-p20b" width="270" align="left" style="padding:0;Margin:0;">
                   <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                     <tr style="border-collapse:collapse;">
                      <td align="left" style="padding:0;Margin:0;padding-top:5px;"> <h2 style="Margin:0;line-height:26px;mso-line-height-rule:exactly;font-family:'trebuchet ms', 'lucida grande', 'lucida sans unicode', 'lucida sans', tahoma, sans-serif;font-size:22px;font-style:normal;font-weight:normal;color:#333333;">{} is here!</h2> </td>
                     </tr>
                     <tr style="border-collapse:collapse;">
                      <td class="es-m-txt-c" align="left" style="padding:0;Margin:0;padding-top:10px;padding-bottom:10px;"> <p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-size:16px;font-family:helvetica, 'helvetica neue', arial, verdana, sans-serif;line-height:24px;color:#333333;">{}</p> </td>
                     </tr>
                     <tr style="border-collapse:collapse;">
                      <td style="padding:0;Margin:0;">
                       <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;">
                         <tr style="border-collapse:collapse;">

                          <td class="es-m-txt-c" width="50%" align="center" style="padding:0;Margin:0;padding-top:10px;"> <span class="es-button-border" style="border-style:solid;border-color:transparent;background:#4FC1CC none repeat scroll 0% 0%;border-width:0px;display:inline-block;border-radius:29px;width:auto;"> <a href="https://viewstripo.email/" class="es-button" target="_blank" style="mso-style-priority:100 !important;text-decoration:none !important;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'comic sans ms', 'marker felt-thin', arial, sans-serif;font-size:16px;color:#FFFFFF;border-style:solid;border-color:#4FC1CC;border-width:5px 15px 5px 15px;display:inline-block;background:#4FC1CC none repeat scroll 0% 0%;border-radius:29px;font-weight:normal;font-style:normal;line-height:19px;width:auto;text-align:center;border-left-width:20px;border-right-width:20px;">Watch it!</a> </span> </td>
                         </tr>
                       </table> </td>
                     </tr>
                   </table> </td>
                 </tr>
               </table>
               <!--[if mso]></td></tr></table><![endif]--> </td>
             </tr>


           </table> </td>
         </tr>
       </table>
""".format(animename,animeurl,eptitle,epfulltitle)
        content2 = content2 + onecontent
    content= content1 + content2 + content3
    return content


def sent_one_email(content,emailaddress):
    import boto3
    from botocore.exceptions import ClientError

    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = "AnimeToday <animetodayservice@gmail.com>"

    # Replace recipient@example.com with a "To" address. If your account
    # is still in the sandbox, this address must be verified.
    RECIPIENT = emailaddress

    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    # CONFIGURATION_SET = "ConfigSet"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "us-east-1"

    # The subject line for the email.
    SUBJECT = "Your New Episodes Today!"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                 "This email was sent with Amazon SES using the "
                 "AWS SDK for Python (Boto)."
                 )

    # The HTML body of the email.
    # BODY_HTML = """<html>
    # <head></head>
    # <body>
    #   <h1>Amazon SES Test (SDK for Python)</h1>
    #   <p>This email was sent with
    #     <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
    #     <a href='https://aws.amazon.com/sdk-for-python/'>
    #       AWS SDK for Python (Boto)</a>.</p>
    # </body>
    # </html>
    #             """
    BODY_HTML = content

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses', region_name=AWS_REGION)
    print('success!')

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

def make_it_text(line):
    content1 = "Hi {} New episodes release! ".format(line[0])
    content2 = ""
    num= 0
    for i in range(len(line[2])):
        animename = line[2][num][0]
        # animeurl = line[2][num][1]
        # eptitle = line[2][num][2]
        epfulltitle = 'https://www.crunchyroll.com' + line[2][num][3]
        num = num + 1
        onecontent = animename + epfulltitle
        content2 = content2 + onecontent
    content = content1 + content2
    return content

def sent_one_text(content, number):
    client = boto3.client("sns")

    # Send your sms message.
    client.publish(Message=content, PhoneNumber=number)

date = '2019-02-01'
rows = get_array(date)
# for line in rows[2:5]:
#     content = make_it_html(line)
#     sent_one_email(content, "animetodayuser@gmail.com")
#     # print(content)

for line in rows[:5]:
    content = make_it_text(line)
    sent_one_text(content, "+18584058857")
# line=[]
# content = make_it_html(line)
# print(content)






