program main;
//compile; inspect streamlines for file 'dpsv.trx'
// fpc main.pas; ./main .\dpsv.trx
{$m+}// directive to be used for using constructor

{$MODE OBJFPC}//or
//{$MODE DELPHI}
uses
  StrUtils,
  SysUtils,
  Zipper,
  Classes,
  trx;

  function runCmd(): boolean;
  var
    fnm: string;
    trx: TTRX;
    i: integer;
  begin
    if (Paramcount < 1) then
    begin
      writeln('No filename provided!');
      exit(False);
    end;
    fnm := ParamStr(1);
    if (not FileExists(fnm)) then
    begin
      writeln('Unable to find the file named ' + fnm);
      exit(False);
    end;
    trx := TTRX.Create(fnm);
    if not trx.ok then
    begin
      trx.Free;
      exit(False);
    end;
    writeln('positions (vertices): ', length(trx.positions) div 3);
    writeln('offsets (streamlines+1) ', length(trx.offsets));
    writeln('statistics (properties + scalars): ', length(trx.scalars));
    if (length(trx.scalars) > 0) then
    begin
      for i := 0 to (length(trx.scalars) - 1) do
      begin
        writeln('statistic', i, ' "', trx.scalars[i].Name, '": ',
          length(trx.scalars[i].scalar));
      end;
    end;
    trx.Free;
    exit(True);
  end; // runCmd()

begin
  runCmd();
end.