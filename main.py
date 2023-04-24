from engine.inference import Inference


knowledgeBaseFile = "G:\FCAI\Third year\second semester\AI\projects\ExpertSystem\Algorithm_Code\Expert-System-master\Expert-System-master\Expert_system_dr_ghazaly\data\diseases\knowledge.json"
clauseBaseFile = "G:\FCAI\Third year\second semester\AI\projects\ExpertSystem\Algorithm_Code\Expert-System-master\Expert-System-master\Expert_system_dr_ghazaly\data\diseases\clause.json"

inferenceEngine = Inference()
inferenceEngine.startEngine(knowledgeBaseFile,
                            clauseBaseFile,
                            verbose=True,
                            method=inferenceEngine.FORWARD)
