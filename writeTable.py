"""
  Function:  writeTable
  --------------------
  momo.sander@googlemail.com
"""                                                  
def writePfam(pfamDict,humProtCod, humChembl, chemblTargets, release):

  out = open('data/pfamTable_%s.tab' % release,'w')
  out.write('target\tnDomains\tpPfam\tsource\n')
  sources = { "ChEMBL, all":chemblTargets, "ChEMBL, human":humChembl, "Ensembl, human":humProtCod}
  for source in sources.keys():
    for target in sources[source].keys():
      if target not in pfamDict.keys():
        out.write('%s\t%s\t%s\t%s\n'%(target, 'NA', 'NA', 'not in Pfam'))
        continue
      if pfamDict[target]['ratio'] == 'NA':
        out.write('%s\t%s\t%s\t%s\n'%(target, 'NA', 'NA', 'no sequence'))
      nDomains = len(pfamDict[target]['domains'])
      pPfam = pfamDict[target]['ratio']
      out.write('%s\t%s\t%s\t%s\n'%(target, nDomains, pPfam, source))
  out.close()


