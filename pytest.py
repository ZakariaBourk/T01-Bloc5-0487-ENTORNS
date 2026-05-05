
import pytest

def test_suma():
    assert 2 + 2 == 5


# Importem les funcions i variables del fitxer original
from Prova_escrita_03 import (
    trobar_edat_maxima,
    trobar_producte_mes_car,
    comptar_empleats_per_departament,
    productes
)

# ex2
@pytest.mark.parametrize(
    "persones, resultat_esperat",
    [
        # Llista correcta amb edats diferents
        (
            [
                {'nom': 'Anna', 'edat': 25},
                {'nom': 'Marc', 'edat': 42},
                {'nom': 'Laura', 'edat': 35}
            ],
            42
        ),
        # Llista buida
        (
            [],
            -1
        ),
        # Falta la clau 'edat'
        (
            [
                {'nom': 'Anna', 'edat': 25},
                {'nom': 'Marc'}
            ],
            -1
        ),
        # Edat no és int
        (
            [
                {'nom': 'Anna', 'edat': '25'},
                {'nom': 'Marc', 'edat': 30}
            ],
            30
        ),
    ]
)
def test_trobar_edat_maxima(persones, resultat_esperat):
    """
    Test de trobar_edat_maxima:
    - comprova edat màxima correcta
    - comprova retorn -1 en llista buida o diccionaris incorrectes
    """
    assert trobar_edat_maxima(persones) == resultat_esperat

# ex3
@pytest.mark.parametrize(
    "llista_productes, resultat_esperat",
    [
        # Cas normal amb diversos productes
        (
            [
                {'nom': 'Producte A', 'preu': 10.0},
                {'nom': 'Producte B', 'preu': 25.5},
                {'nom': 'Producte C', 'preu': 18.0}
            ],
            {'nom': 'Producte B', 'preu': 25.5}
        ),
        # Cas de llista buida
        (
            [],
            None
        ),
    ]
)
def test_trobar_producte_mes_car(llista_productes, resultat_esperat):
    """
    Test de trobar_producte_mes_car:
    - retorna el producte més car
    - retorna None si la llista està buida
    """
    # Modifiquem la variable global productes
    productes.clear()
    productes.extend(llista_productes)

    resultat = trobar_producte_mes_car()
    assert resultat == resultat_esperat

#ex4
@pytest.mark.parametrize(
    "empresa, resultat_esperat",
    [
        # Empresa amb diversos departaments i empleats
        (
            {
                'nom': 'Empresa X',
                'departaments': [
                    {
                        'nom': 'IT',
                        'empleats': [{'nom': 'A'}, {'nom': 'B'}]
                    },
                    {
                        'nom': 'HR',
                        'empleats': [{'nom': 'C'}]
                    }
                ]
            },
            {
                'IT': 2,
                'HR': 1
            }
        ),
        # Empresa sense departaments
        (
            {
                'nom': 'Empresa Buida',
                'departaments': []
            },
            {}
        ),
    ]
)
def test_comptar_empleats_per_departament(empresa, resultat_esperat):
    """
    Test de comptar_empleats_per_departament:
    - comprova el nombre d'empleats per departament
    - comprova que funcioni amb llista buida de departaments
    """
    resultat = comptar_empleats_per_departament(empresa)
    assert resultat == resultat_esperat
