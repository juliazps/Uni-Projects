// 1. Modelo de Assento
class Assento {
    private String id;
    private boolean ocupado;

    public Assento(String id) {
        this.id = id;
        this.ocupado = false;
    }

    public String getId() {
        return id;
    }

    public boolean isOcupado() {
        return ocupado;
    }

    public void reservar() {
        ocupado = true;
    }

    @Override
    public String toString() {
        return ocupado ? "[X]" : "[" + id + "]";
    }
}

// 2. Classe Cinema com os assentos e lógica principal
import java.util.*;

public class Cinema {
    private Assento[][] cadeiras = new Assento[5][5];
    private Scanner sc = new Scanner(System.in);
    private List<String> alimentos = Arrays.asList("Pipoca", "Refrigerante", "Chocolate");
    private List<String> carrinhoAlimentos = new ArrayList<>();

    public Cinema() {
        char fileira = 'A';
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                cadeiras[i][j] = new Assento(fileira + "" + (j + 1));
            }
            fileira++;
        }
    }

    public void iniciar() {
        mostrarAssentos();
        escolherAssentos();
        escolherAlimentos();
        escolherPagamento();
    }

    private void mostrarAssentos() {
        System.out.println("Assentos disponíveis:");
        for (Assento[] fileira : cadeiras) {
            for (Assento a : fileira) {
                System.out.print(a + " ");
            }
            System.out.println();
        }
    }

    private void escolherAssentos() {
        while (true) {
            System.out.print("Digite o assento que deseja (ex: A1) ou 'fim' para terminar: ");
            String escolha = sc.nextLine().toUpperCase();

            if (escolha.equals("FIM")) break;

            boolean reservado = false;

            for (Assento[] fileira : cadeiras) {
                for (Assento a : fileira) {
                    if (a.getId().equals(escolha)) {
                        if (!a.isOcupado()) {
                            a.reservar();
                            System.out.println("Assento " + escolha + " reservado com sucesso.");
                            reservado = true;
                        } else {
                            System.out.println("Assento já está ocupado.");
                        }
                    }
                }
            }

            if (!reservado) System.out.println("Assento inválido.");
            mostrarAssentos();
        }
    }

    private void escolherAlimentos() {
        System.out.println("\n--- Cardápio ---");
        for (int i = 0; i < alimentos.size(); i++) {
            System.out.println((i + 1) + " - " + alimentos.get(i));
        }

        while (true) {
            System.out.print("Escolha um item (número) ou 0 para finalizar: ");
            int escolha = sc.nextInt();
            sc.nextLine(); // limpa buffer

            if (escolha == 0) break;
            if (escolha > 0 && escolha <= alimentos.size()) {
                carrinhoAlimentos.add(alimentos.get(escolha - 1));
                System.out.println(alimentos.get(escolha - 1) + " adicionado ao carrinho.");
            } else {
                System.out.println("Opção inválida.");
            }
        }
    }

    private void escolherPagamento() {
        System.out.println("\n--- Formas de Pagamento ---");
        System.out.println("1 - Cartão");
        System.out.println("2 - Dinheiro");
        System.out.println("3 - Pix");

        System.out.print("Escolha a forma de pagamento: ");
        int escolha = sc.nextInt();
        sc.nextLine(); // limpa buffer

        String forma = switch (escolha) {
            case 1 -> "Cartão";
            case 2 -> "Dinheiro";
            case 3 -> "Pix";
            default -> "Desconhecida";
        };

        System.out.println("Pagamento via " + forma + " selecionado.");
        System.out.println("Compra finalizada! Aproveite o filme 🎬");
    }
}

//3. Main
public class Main {
    public static void main(String[] args) {
        Cinema cinema = new Cinema();
        cinema.iniciar();
    }
}
