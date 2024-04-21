# XTuner 소개

XTuner는 효율적이고 유연하며 기능이 풍부한 대규모 모델 파인튜닝 도구 키트입니다.

## 지원 모델

- Llama 3 모델 (2024년 4월 추가)
- Gemma 모델 (2024년 2월 추가) 
- Qwen 1.5 모델 (2024년 2월 추가)
- InternLM2 모델 (2024년 1월 추가)
- DeepSeek-MoE 모델 (2024년 1월 추가)
- ChatGLM3-6B 모델 (2023년 11월 추가)
- InternLM-20B 모델 (2023년 9월 추가)
- Baichuan2 모델 (2023년 9월 추가)
- LLaVA 1.5 아키텍처 기반 VLM 모델 (2023년 12월 추가)
- Mixtral 8x7B 모델 (2023년 12월 추가)
- 기타 다양한 LLM 모델 (InternLM, Llama 2, ChatGLM, Qwen 등)

## 주요 기능

- 거의 모든 GPU에서 LLM, VLM 사전 학습 및 파인튜닝 지원
- 단일 8GB GPU에서 7B LLM 파인튜닝 가능
- 70B 이상 모델의 다중 노드 파인튜닝 지원
- FlashAttention, Triton 커널 등 고성능 연산자 자동 디스패치로 훈련 처리량 증대
- DeepSpeed와 호환되어 다양한 ZeRO 최적화 기술 활용 가능
- 잘 설계된 데이터 파이프라인으로 다양한 포맷의 데이터셋 수용
- QLoRA, LoRA, 전체 파라미터 파인튜닝 등 다양한 학습 알고리즘 지원
- 대규모 모델과의 지속적인 사전 학습, 명령어 파인튜닝, 에이전트 파인튜닝 지원 
- 사전 정의된 템플릿으로 대규모 모델과 챗 기능 제공
- 결과 모델이 배포 및 서버 도구(LMDeploy), 대규모 평가 도구(OpenCompass, VLMEvalKit)와 원활히 통합 가능



[xtuner](https://github.com/ox1111/xtuner.git)
