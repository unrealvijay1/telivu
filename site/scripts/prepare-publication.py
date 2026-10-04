"""Export website source only; never copies application history or release artifacts."""
from pathlib import Path
import shutil
import xml.etree.ElementTree as ET

repo = Path(__file__).resolve().parents[2]
site = repo/'site'
output = repo/'artifacts'/'telivu-publish'
if output.exists():
 raise SystemExit('Publish folder already exists. Preserve it; choose a new export location before regenerating.')
version = ET.parse(repo/'Directory.Build.props').findtext('.//ProductVersion')
output.mkdir(parents=True)
files = []
for source in sorted(site.rglob('*')):
 if not source.is_file() or any(p in {'_build','__pycache__','.git'} for p in source.relative_to(site).parts): continue
 if source.is_symlink(): raise SystemExit('Symlinks are not exported')
 relative = source.relative_to(repo)
 target = output/relative; target.parent.mkdir(parents=True,exist_ok=True)
 shutil.copyfile(source,target); files.append(relative.as_posix())
workflow = Path('.github/workflows/pages.yml')
(output/workflow).parent.mkdir(parents=True,exist_ok=True)
shutil.copyfile(repo/workflow,output/workflow);files.append(workflow.as_posix())
project = ET.Element('Project')
ET.SubElement(ET.SubElement(project,'PropertyGroup'),'ProductVersion').text = version
ET.indent(project)
ET.ElementTree(project).write(output/'Directory.Build.props',encoding='utf-8',xml_declaration=True)
files.append('Directory.Build.props')
(output/'.gitignore').write_text('site/_build/\n**/__pycache__/\nartifacts/\n',encoding='utf-8')
files.append('.gitignore')
manifest = repo/'artifacts'/'telivu-publish-files.txt'
manifest.write_text('\n'.join(sorted(files))+'\n',encoding='utf-8')
assert not (output/'.git').exists()
assert len(list(output.rglob('*'))) > 0
print(f'Prepared {len(files)} source files in {output}')
print(f'Exact source inventory: {manifest}')
