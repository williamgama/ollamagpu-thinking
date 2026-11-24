# Gama Build Lab

Ambiente reutilizável de compilação remota de software público com GitHub Actions, independente da infraestrutura de produção da Gama Corp.

## Builds

- **OllamaGPU Thinking (macOS Intel):** [workflow](.github/workflows/ollama-thinking-build.yml). Compila somente a interface desktop de uma revisão fixa do fork, com correção upstream para controles de raciocínio. Não compila nem distribui pesos ou o motor Vulkan. Artefato experimental; validação no Mac ainda necessária.

## Convenções

- Um workflow isolado por projeto e plataforma, com disparo manual e permissões mínimas.
- Fixar revisões de código e patches; validar arquitetura e registrar origem, checksum SHA-256 e testes de cada artefato.
- Priorizar runners padrão hospedados pelo GitHub, com limites de tempo e retenção de artefatos.
- Não publicar código privado, credenciais, dados de clientes ou configurações internas neste repositório público. Builds privados exigem ambiente separado e orçamento verificado.
- Preservar instalações funcionais; instalar artefatos experimentais somente em cópias reversíveis.

Nome planejado do repositório: `gama-build-lab`. Renomear após a execução inicial, mantendo histórico e workflows.
