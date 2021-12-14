from tir import Webapp
import dados_Pedido  as CE
import dados_Prod as prod
from datetime import *
import unittest

data_atual = date.today()
data_atual_str = data_atual.strftime('%d/%m/%Y')#diretivas do objeto data_atual	



class MODULO(unittest.TestCase):
	

	@classmethod
	def setUpClass(inst):

		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT',data_atual_str,'01','0101 ','99')

		inst.oHelper.Program('MATA410')
		# inst.oHelper.SetLateralMenu('Usuário > Senhas > Usuários')
		# inst.oHelper.SearchBrowse('000011')
		# inst.oHelper.SetButton('Outras Ações')
		# inst.oHelper.SetKey('DOWN',grid=False,grid_number=5)
		
	
	def test_MATA410(self):	
    	
    	
		linha = 0
		linha_produto =0
		
		#self.oHelper.SetButton('Fechar')
		a = 1
		while linha < CE.lin:
			

			self.oHelper.SetButton('Incluir')
			self.oHelper.SetBranch('0102')
			#self.oHelper.SetButton('Ok')
			
			#self.oHelper.ClickFolder('Grupo')

			#self.oHelper.SetValue(CE.CABECALHO[0],CE.COL_A[linha])
			self.oHelper.SetValue(CE.CABECALHO[1],CE.COL_B[linha])
			self.oHelper.SetValue(CE.CABECALHO[2],CE.COL_C[linha])
			self.oHelper.SetValue(CE.CABECALHO[3],CE.COL_D[linha])
			self.oHelper.SetValue(CE.CABECALHO[4],CE.COL_E[linha])
			self.oHelper.SetValue(CE.CABECALHO[5],CE.COL_F[linha])
			self.oHelper.SetValue(CE.CABECALHO[6],CE.COL_G[linha])
			self.oHelper.SetValue(CE.CABECALHO[7],CE.COL_H[linha])
			self.oHelper.SetValue(CE.CABECALHO[8],CE.COL_I[linha])

			
			while linha_produto < prod.lin:

			################# INSERIR PRODUTOS ####################
				#self.oHelper.ClickGridHeader(column_name = 'Produto' , grid_number =  1)
				



				self.oHelper.SetValue(prod.CABECALHO[0],prod.COL_A[linha_produto], grid=True)
				self.oHelper.SetValue(prod.CABECALHO[1],prod.COL_B[linha_produto], grid=True)
				self.oHelper.SetValue(prod.CABECALHO[2],prod.COL_C[linha_produto], grid=True)
				self.oHelper.SetValue(prod.CABECALHO[3],prod.COL_D[linha_produto], grid=True)
				self.oHelper.SetValue(prod.CABECALHO[4],prod.COL_E[linha_produto], grid=True)
				#self.oHelper.SetValue(prod.CABECALHO[5],prod.COL_F[linha], grid=True)
				# self.oHelper.SetValue(prod.CABECALHO[6],prod.COL_G[linha], grid=True)
				# self.oHelper.SetValue(prod.CABECALHO[7],prod.COL_H[linha], grid=True)
				
				self.oHelper.SetKey('DOWN', grid=True)

				linha_produto = linha_produto + 1

			self.oHelper.LoadGrid()
			self.oHelper.SetButton("Salvar")
			self.oHelper.SetButton("Salvar")
			#self.oHelper.SetButton("Cancelar")
			

			# self.oHelper.SearchBrowse(f'D MG    {cliente+loja}', 'Filial+codigo + Loja')
			
			# self.oHelper.SetButton('Visualizar')
			# self.oHelper.ClickFolder('Cadastrais')
			# self.oHelper.CheckResult('A1_COD',cliente)
			# self.oHelper.CheckResult('A1_LOJA',loja)
			# self.oHelper.CheckResult('A1_PESSOA','F - Fisica')
			# self.oHelper.CheckResult('A1_NOME','FAT TIR CT133 MATA030 INCLUSAO')
			# self.oHelper.CheckResult('A1_NREDUZ','TIR CT133 MATA030')
			# self.oHelper.CheckResult('A1_END','RUA DAS ORQUIDEAS, 100')
			# self.oHelper.CheckResult('A1_TIPO','F - Cons.Final')
			# self.oHelper.CheckResult('A1_EST','SP')
			# self.oHelper.CheckResult('A1_COD_MUN','50308')
			# self.oHelper.SetButton('Cancelar')
			linha = linha + 1
			
		# self.oHelper.SetValue('C5_VEND2','')

		# self.oHelper.SetButton('Outras Ações')

		
		
		self.oHelper.AssertTrue()
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()