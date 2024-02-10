export interface Question {
  question_id: number;
  question: string;
  answer: string | null;
  question_type: 'text' | 'choice';
  choices: Choice[];
}

interface Choice {
  // Define properties of the Choice model here
  text: string;
}
