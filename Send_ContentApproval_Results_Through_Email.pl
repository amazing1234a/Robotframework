use Mail::Sender;
$File ='C:\/socialite_automation\/ContentApproval\/Results\/ContentApprovalResults.xls';

my $FacebookResults = `ReadCSVs.pl $File`;

$FacebookResultslength= length($FacebookResults);
if($FacebookResultslength>0)
{ 
$ContentApproval= "ContentApproval: \n \n $FacebookResults";
$Subject="Auto Generated email on ContentApproval Automation Results Daily run";
print $ContentApproval;
$to_list ="automationuser\@socauto.local";

eval
{ 
   $Sender = new Mail::Sender
   {smtp => '192.168.120.250', from => "Automation-team\@actiance.com"};
   $Sender->MailMsg({to =>"$to_list",
   cc =>"$cc_mail",   
   subject => $Subject,
   msg => $ContentApproval,
   });
   $sender-> close() or print "Cannot send mail: $Mail::Sender::Error\n";  
} 
}




