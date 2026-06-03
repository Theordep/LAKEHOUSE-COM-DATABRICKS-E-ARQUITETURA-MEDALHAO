# Databricks Job — pipeline sequencial

## Criar a Job manualmente (UI)

1. **Workflows** → **Create Job**.
2. Nome: `medalhao_seguros_pipeline`.
3. Adicione tarefas do tipo **Notebook**, na ordem:

| Ordem | Notebook | Descrição |
|-------|----------|-----------|
| 1 | `notebooks/000_validar_landing` | Valida CSVs no Volume |
| 2 | `notebooks/001_preparar_ambiente` | Cria schemas e volume |
| 3 | `notebooks/002_bronze` | Bronze Delta |
| 4 | `notebooks/003_silver` | Silver + DQ |
| 5 | `notebooks/004_gold` | Gold Kimball |

4. Em cada tarefa (exceto a primeira), configure **Depends on** a tarefa anterior.
5. Cluster: qualquer cluster **Single Node** compatível com Free Edition.
6. **Run now**.

## Referência JSON

O arquivo `jobs/medalhao_pipeline.job.yml` descreve a mesma sequência para importação ou documentação.

!!! note "Pré-requisito"
    Os 11 CSVs devem estar em `/Volumes/workspace/landing/dados/` antes de executar a Job.
    Use `python3 scripts/extract_to_landing.py` localmente e faça upload pelo UI do Volume.

## Notebook 005

`005_destruir_ambiente.py` remove schemas (`landing`, `bronze`, `silver`, `gold`). **Não** inclua na Job de produção; use apenas para limpar o ambiente após testes.
